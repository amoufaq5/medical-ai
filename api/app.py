# api/app.py

from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model("model/diagnostic_model.h5")

# Dummy tokenizer function (in production, use a proper tokenizer)
def dummy_text_preprocess(text):
    return [ord(c) % 100 for c in text][:50]

@app.route("/diagnose", methods=["POST"])
def diagnose():
    data = request.json
    text_input = data.get("text", "")
    # In production, also accept image file and lab test data
    # For this demo, generate a dummy image input
    image_input = np.random.rand(224, 224, 3)
    
    # Preprocess text input
    seq = dummy_text_preprocess(text_input)
    seq_padded = pad_sequences([seq], padding="post", maxlen=50)
    
    # Prepare model inputs
    prediction = model.predict({"text_input": seq_padded, "image_input": np.array([image_input])})
    # Map prediction to a disease (dummy mapping for demo)
    disease_mapping = ["pneumonia", "asthma", "CVD", "common cold", "flu", "covid", "bronchitis", "influenza"]
    predicted_disease = disease_mapping[np.argmax(prediction)]
    
    response = {
        "diagnosis": predicted_disease,
        "confidence": float(np.max(prediction))
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
