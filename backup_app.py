from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from mediapipe import solutions as mp_solutions
from collections import deque
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 30 * 1024 * 1024  # 30 MB

# Load the pre-trained model (make sure it is compatible with your TensorFlow version)
try:
    model = tf.saved_model.load('saved_model')
except Exception as e:
    print(f"Error: {e}")

# Constants
SEQUENCE_LENGTH = 30  # Frames per sequence

# Initialize a buffer to store sequences of keypoints
sequence_buffer = deque(maxlen=SEQUENCE_LENGTH)
ACTIONS = np.array(['Hi', 'Saya Sayang Awak', 'Makan',
                   'Selamat Malam', 'Terima Kasih', 'Apa Khabar',
                   'Awak', 'Saya', 'Minum',
                   'Salah', 'Betul', 'Minta Maaf',
                   'Tolong', 'Hijau', 'Kita',
                   'Mereka', 'Ini', 'Itu',
                   'Apa', 'Siapa'])

# Initialize Mediapipe holistic solution
mp_holistic_instance = mp_solutions.holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)

def extract_keypoints_from_dict(keypoints):
    """
    Extracts keypoints from the `keypoints` dictionary received from the frontend.

    Args:
        keypoints (dict): A dictionary containing pose, leftHand, and rightHand keypoints.

    Returns:
        np.ndarray: A concatenated array of pose, left hand, and right hand keypoints.
    """
    # Pose keypoints (33 landmarks with x, y, z, visibility)
    pose = (
        np.array([[p['x'], p['y'], p['z'], p['visibility']] for p in keypoints.get('pose', [])])
        if 'pose' in keypoints and keypoints['pose']
        else np.zeros((33, 4))  # Default zero-padding if pose data is missing
    )

    # Left hand keypoints (21 landmarks with x, y, z)
    left_hand = (
        np.array([[lh['x'], lh['y'], lh['z']] for lh in keypoints.get('leftHand', [])])
        if 'leftHand' in keypoints and keypoints['leftHand']
        else np.zeros((21, 3))  # Default zero-padding if left hand data is missing
    )

    # Right hand keypoints (21 landmarks with x, y, z)
    right_hand = (
        np.array([[rh['x'], rh['y'], rh['z']] for rh in keypoints.get('rightHand', [])])
        if 'rightHand' in keypoints and keypoints['rightHand']
        else np.zeros((21, 3))  # Default zero-padding if right hand data is missing
    )

    # Flatten and concatenate all keypoints
    return np.concatenate([pose.flatten(), left_hand.flatten(), right_hand.flatten()])

def make_prediction(keypoints_sequence):
    """Make a prediction using the loaded model."""
    try:
        # Ensure the input sequence is a tensor of the correct shape
        input_tensor = tf.convert_to_tensor(keypoints_sequence, dtype=tf.float32)
        # print("Converted keypoints sequence to tensor.")

        try:
            # Get the model inference function (assuming it's a saved model with 'serving_default' signature)
            infer = model.signatures['serving_default']
        except KeyError as e:
            print(f"Error: Model does not have 'serving_default' signature. Exception: {e}")
            return None

        try:
            # Perform prediction
            prediction = infer(input_tensor)
            print(f"Prediction: {prediction}")
        except Exception as e:
            print(f"Error during inference: {e}")
            return None

        # Check if the model returns a dictionary, and handle accordingly
        try:
            if isinstance(prediction, dict):
                output_tensor = prediction.get('output_0')  # Adjust this if needed
            else:
                output_tensor = prediction

            if output_tensor is None:
                raise ValueError("Model output 'output_0' is not found or prediction failed.")
        except Exception as e:
            print(f"Error handling model output: {e}")
            return None

        return output_tensor

    except Exception as e:
        print(f"Error during prediction: {e}")
        return None

@app.route('/predict', methods=['POST'])
def predict_action():
    """Handles the action prediction from the keypoints."""
    try:
        # Extract keypoints from the request JSON payload
        keypoints = request.json.get("keypoints")  # Get keypoints from the request
        if not keypoints:
            return jsonify({"error": "No keypoints received."}), 400

        # Ensure keypoints are in the correct format (numpy array)
        keypoints_array = extract_keypoints_from_dict(keypoints)
        # print(f"Keypoints shape: {keypoints_array.shape}")

        # Add the keypoints to the sequence buffer
        sequence_buffer.append(keypoints_array)

        # If we don't yet have a full sequence, return an error
        if len(sequence_buffer) < SEQUENCE_LENGTH:
            return jsonify({"error": "Not enough keypoints to make a prediction."}), 400

        # Form the input tensor by stacking the buffered sequences
        keypoints_sequence = np.array(sequence_buffer)  # Shape: (SEQUENCE_LENGTH, feature_size)
        keypoints_sequence = np.expand_dims(keypoints_sequence, axis=0)  # Add batch dimension, Shape: (1, SEQUENCE_LENGTH, feature_size)

        # print(f"Prepared input tensor shape: {keypoints_sequence.shape}")

        # Make the prediction using the model
        prediction = make_prediction(keypoints_sequence)

        if prediction is not None:
            predicted_action = ACTIONS[np.argmax(prediction.numpy())]  # Get the predicted action
            confidence = float(np.max(prediction.numpy()))  # Get the confidence
            print(f"Predicted action: {predicted_action}, Confidence: {confidence}")
            return jsonify({"action": predicted_action, "confidence": confidence})

        else:
            print("Prediction failed.")
            return jsonify({"error": "Prediction failed."}), 500

    except Exception as e:
        print(f"Error in predict_action function: {e}")
        return jsonify({"error": "Error in processing keypoints"}), 500

if __name__ == '__main__':
    try:
        print("Starting Flask app...")
        app.run(debug=True, port=5000)
    except Exception as e:
        print(f"Error starting Flask app: {e}")
