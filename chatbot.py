from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pyngrok import ngrok
import os
import time
import fine_tuning_data

# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Configure Google GEMINI API
API_KEY = "Skibidi Toilet"  # Replace with your actual Google PaLM API key
genai.configure(api_key=API_KEY)

base_model = "models/gemini-1.5-flash-001-tuning"
tuned_model = "tunedModels/increment-dqus340j2kzg"
model = genai.GenerativeModel(model_name=tuned_model)


def fine_tune():
    operation = genai.create_tuned_model(
        display_name="increment",
        source_model=base_model,
        epoch_count=20,
        batch_size=4,
        learning_rate=0.001,
        training_data=fine_tuning_data.diverse_training_data,
    )

    for status in operation.wait_bar():
        time.sleep(10)

    result = operation.result()
    print(result)
    
    # Plot the loss curve
    snapshots = pd.DataFrame(result.tuning_task.snapshots)
    sns.lineplot(data=snapshots, x='epoch', y='mean_loss')
    plt.title('Fine-tuning Loss Curve')
    plt.savefig('loss_curve.png')  # Save the plot as an image
    plt.show()  # Display the plot

    model = genai.GenerativeModel(model_name=result.name, system_instruction="You are Echo, an AI assistant for Echo Sign, an innovative online video meeting platform that integrates a sign language recognition AI model. Your primary role is to assist users by answering their questions and guiding them on how to use the platform's features. Echo Sign is designed to bridge communication barriers between deaf and hearing individuals by recognizing sign language gestures and displaying the detected actions as text beneath the video section of the deaf person's screen.")
    result = model.generate_content("How to turn on the sign language recognition feature")
    print(result.text)

def get_fine_tune_models():
    for model_info in genai.list_tuned_models():
        print(model_info.name)

@app.route("/")
def home():
    return "Chatbot backend powered by Google PaLM (Gemini) is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Explicitly send the system instruction as part of the first user message
        chat = model.start_chat()
        first_message = f"You are Echo, an AI assistant for Echo Sign, an innovative online video meeting platform that integrates a sign language recognition AI model. Your primary role is to assist users by answering their questions and guiding them on how to use the platform's features. Echo Sign is designed to bridge communication barriers between deaf and hearing individuals by recognizing sign language gestures and displaying the detected actions as text beneath the video section of the deaf person's screen.\n\nUser: {user_message}"
        response = chat.send_message(first_message) # Include system instruction
        bot_reply = response.text
    except Exception as e:
        bot_reply = f"Error: {str(e)}"

    return jsonify({"response": bot_reply})


if __name__ == '__main__':
    try:
        print("Starting Flask app...")
        # fine_tune()
        get_fine_tune_models()
        app.run(host='10.131.73.75', port=5000, debug=True)  # Specify IP and port
    except Exception as e:
        print(f"Error starting Flask app: {e}")
