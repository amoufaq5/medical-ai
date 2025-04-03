# model/train.py

import numpy as np
import tensorflow as tf
from model.model import build_multimodal_model
import pandas as pd
from sklearn.model_selection import train_test_split, KFold

def dummy_text_preprocess(text):
    # Placeholder: convert text to sequence of integers
    # In production, use a proper tokenizer (e.g., tf.keras.preprocessing.text.Tokenizer)
    return [ord(c) % 100 for c in text][:50]  # limit sequence length

def dummy_image_preprocess(image_path):
    # Placeholder: load and preprocess image from file
    # In production, use image loading and preprocessing libraries
    return np.random.rand(224, 224, 3)

def load_dataset():
    # For simplicity, we load the CSV dataset and generate dummy features.
    df = pd.read_csv("dataset/data.csv")
    # Generate dummy text sequences and dummy images for each row
    texts = df["overview"].apply(dummy_text_preprocess).tolist()
    images = [np.random.rand(224, 224, 3) for _ in range(len(texts))]
    # Dummy labels: one-hot encoded (in production, map diseases to indices)
    labels = np.eye(8)[np.arange(len(df)) % 8]
    return np.array(texts, dtype=object), np.array(images), labels

def train_model():
    texts, images, labels = load_dataset()
    
    # In production, pad the text sequences to uniform length
    texts_padded = tf.keras.preprocessing.sequence.pad_sequences(texts, padding='post', maxlen=50)
    
    model = build_multimodal_model()
    
    # Use KFold cross-validation for evaluation
    kf = KFold(n_splits=5)
    fold = 1
    for train_index, test_index in kf.split(texts_padded):
        x_train_text = texts_padded[train_index]
        x_train_img = images[train_index]
        y_train = labels[train_index]
        
        x_test_text = texts_padded[test_index]
        x_test_img = images[test_index]
        y_test = labels[test_index]
        
        print(f"Training fold {fold}")
        model.fit(
            {"text_input": x_train_text, "image_input": x_train_img},
            y_train,
            epochs=5,  # adjust epochs as needed
            batch_size=4
        )
        loss, acc = model.evaluate(
            {"text_input": x_test_text, "image_input": x_test_img},
            y_test
        )
        print(f"Fold {fold} - Loss: {loss}, Accuracy: {acc}")
        fold += 1

    # Save the trained model for inference
    model.save("model/diagnostic_model.h5")
    print("Model training complete and saved.")

if __name__ == "__main__":
    train_model()
