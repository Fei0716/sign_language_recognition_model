from flask import Flask, request, jsonify
import cv2
import numpy as np
import tensorflow as tf
from mediapipe import solutions as mp_solutions

app = Flask(__name__)
# Set maximum content length to 50 MB (adjust as needed)
app.config['MAX_CONTENT_LENGTH'] = 30 * 1024 * 1024  # 30 MB

# Load the pre-trained model (make sure it is compatible with your TensorFlow version)
try:
    model = tf.saved_model.load('saved_model')
except Exception as e:
    print(f"Error: {e}")

# Mediapipe setup
mp_holistic = mp_solutions.holistic

# Constants
SEQUENCE_LENGTH = 30  # Frames per sequence
ACTIONS = np.array(['Hi', 'Saya Sayang Awak', 'Makan',
                   'Selamat Malam', 'Terima Kasih', 'Apa Khabar',
                   'Awak', 'Saya', 'Minum',
                   'Salah', 'Betul', 'Minta Maaf',
                   'Tolong', 'Hijau', 'Kita',
                   'Mereka', 'Ini', 'Itu',
                   'Apa', 'Siapa'])

# Initialize sequence buffer
sequence = []

mp_holistic_instance = mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)
# def process_frame(frame):
#     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     results = mp_holistic_instance.process(frame_rgb)
#     return extract_keypoints(results)
#
# def extract_keypoints(results):
#     """Extracts keypoints from MediaPipe results."""
#     pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33 * 4)
#     lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21 * 3)
#     rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21 * 3)
#     return np.concatenate([pose, lh, rh])
#
# def make_prediction(input_sequence):
#     """Make a prediction using the loaded model."""
#     try:
#         # Use the 'serving_default' signature
#         infer = model.signatures['serving_default']
#         input_tensor = tf.convert_to_tensor(input_sequence, dtype=tf.float32)
#
#         # Perform prediction
#         prediction = infer(input_tensor)
#
#         # Return the output
#         return prediction
#     except Exception as e:
#         print(f"Error during prediction: {e}")
#         return None
#
#
# # prediction using frames(images)
# @app.route('/predict', methods=['POST'])
# def predict_action():
#     """API endpoint to predict the action based on the sequence of frames."""
#     global sequence  # Use the global sequence buffer
#
#     # Collect all frames from the request
#     for key in sorted(request.files.keys()):  # Ensure frame order
#         file = request.files[key]
#         np_frame = np.frombuffer(file.read(), np.uint8)
#         frame = cv2.imdecode(np_frame, cv2.IMREAD_COLOR)
#         keypoints = process_frame(frame)
#
#         # Append keypoints to the sequence
#         sequence.append(keypoints)
#
#         # Ensure the sequence length does not exceed the desired length
#         if len(sequence) > SEQUENCE_LENGTH:
#             sequence.pop(0)  # Remove the oldest frame (FIFO)
#
#         # print(f"Current Sequence Length: {len(sequence)}")
#
#     # If we have collected a full sequence (30 frames), make the prediction
#     if len(sequence) == SEQUENCE_LENGTH:
#         sequence_array = np.expand_dims(sequence, axis=0).astype(np.float32)  # Expand dims for batch
#
#         try:
#             # Make prediction using the model
#             prediction = make_prediction(sequence_array)  # Use the saved model function
#             if prediction is not None:
#                 # Extract prediction result using the correct output key 'output_0'
#                 predicted_action = ACTIONS[np.argmax(prediction['output_0'].numpy())]
#                 print(f"Predicted Action: {predicted_action}")
#
#                 # Return prediction with action and confidence
#                 confidence = float(np.max(prediction['output_0'].numpy()))
#                 print(f"Confidence: {confidence}")
#
#                 # Clear the sequence buffer after prediction
#                 sequence.clear()
#
#                 return jsonify({
#                     "action": predicted_action,
#                     "confidence": confidence
#                 })
#             else:
#                 return jsonify({"error": "Prediction failed."}), 500
#         except Exception as e:
#             return jsonify({"error": f"Prediction failed: {str(e)}"}), 500
#
#     # If the sequence is not yet complete
#     return jsonify({"error": "Incomplete sequence, waiting for more frames."}), 400

#prediction using keypoints
def preprocess_keypoints(keypoints_data):
    """Preprocess the received keypoints into a flattened array."""
    pose = np.array(keypoints_data.get('pose', []), dtype=np.float32).flatten()
    left_hand = np.array(keypoints_data.get('leftHand', []), dtype=np.float32).flatten()
    right_hand = np.array(keypoints_data.get('rightHand', []), dtype=np.float32).flatten()

    # Ensure dimensions match expectations
    pose = pose[:33 * 4] if pose.size >= 33 * 4 else np.zeros(33 * 4)
    left_hand = left_hand[:21 * 3] if left_hand.size >= 21 * 3 else np.zeros(21 * 3)
    right_hand = right_hand[:21 * 3] if right_hand.size >= 21 * 3 else np.zeros(21 * 3)

    # Concatenate all keypoints into a single array
    return np.concatenate([pose, left_hand, right_hand])

def make_prediction(input_sequence):
    """Make a prediction using the TensorFlow model."""
    try:
        if not model:
            raise ValueError("Model is not loaded.")

        # Use the 'serving_default' signature to predict
        infer = model.signatures['serving_default']
        input_tensor = tf.convert_to_tensor(input_sequence, dtype=tf.float32)
        prediction = infer(input_tensor)

        # Return the output
        return prediction
    except Exception as e:
        print(f"Error during prediction: {e}")
        return None

@app.route('/predict-keypoints', methods=['POST'])
def predict_action():
    """API endpoint to predict the action based on sequences of keypoints."""
    global sequence

    if not model:
        return jsonify({"error": "Model not loaded."}), 500

    try:
        # Validate the input
        data = request.json
        if not data or 'keypoints' not in data:
            return jsonify({"error": "Keypoints data is required in the request body."}), 400

        keypoints = data['keypoints']

        # Preprocess keypoints into a flattened array
        keypoints_flattened = preprocess_keypoints(keypoints)

        # Validate the flattened keypoints length
        if keypoints_flattened.size != 258:
            return jsonify({"error": f"Flattened keypoints must have a length of 258, got {keypoints_flattened.size}."}), 400

        # Add keypoints to the sequence
        sequence.append(keypoints_flattened)

        # Ensure sequence length does not exceed SEQUENCE_LENGTH
        if len(sequence) > SEQUENCE_LENGTH:
            sequence.pop(0)

        # If the sequence is complete, make a prediction
        if len(sequence) == SEQUENCE_LENGTH:
            input_sequence = np.expand_dims(sequence, axis=0).astype(np.float32)

            # Make prediction
            prediction = make_prediction(input_sequence)
            if prediction is not None:
                # Extract prediction results
                output_probs = prediction['output_0'].numpy()[0]  # Assuming 'output_0' is correct
                predicted_index = np.argmax(output_probs)
                predicted_action = ACTIONS[predicted_index]
                confidence = float(output_probs[predicted_index])

                # Clear sequence buffer after prediction
                sequence.clear()

                return jsonify({
                    "action": predicted_action,
                    "confidence": confidence
                })
            else:
                return jsonify({"error": "Failed to make prediction."}), 500

        # If sequence is incomplete
        return jsonify({"message": "Keypoints added to sequence.", "current_length": len(sequence)}), 200

    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    try:
        print("Starting Flask app...")
        app.run(debug=True)
    except Exception as e:
        print(f"Error starting Flask app: {e}")
