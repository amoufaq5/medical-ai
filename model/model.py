# model/model.py

import tensorflow as tf
from tensorflow.keras import layers, models

def build_text_model(input_dim=100, embedding_dim=64):
    # Simple text submodel using embedding and LSTM
    text_input = layers.Input(shape=(None,), name="text_input")
    x = layers.Embedding(input_dim=input_dim, output_dim=embedding_dim)(text_input)
    x = layers.LSTM(32)(x)
    text_output = layers.Dense(16, activation='relu')(x)
    return text_input, text_output

def build_image_model(input_shape=(224, 224, 3)):
    # Simple CNN for image processing
    image_input = layers.Input(shape=input_shape, name="image_input")
    x = layers.Conv2D(32, (3, 3), activation='relu')(image_input)
    x = layers.MaxPooling2D((2, 2))(x)
    x = layers.Conv2D(64, (3, 3), activation='relu')(x)
    x = layers.MaxPooling2D((2, 2))(x)
    x = layers.Flatten()(x)
    image_output = layers.Dense(16, activation='relu')(x)
    return image_input, image_output

def build_multimodal_model():
    text_input, text_features = build_text_model()
    image_input, image_features = build_image_model()
    
    # Combine the features from both modalities
    combined = layers.concatenate([text_features, image_features])
    x = layers.Dense(32, activation='relu')(combined)
    # Output: diagnostic predictions (for example, probabilities over disease classes)
    output = layers.Dense(8, activation='softmax', name="diagnosis_output")(x)
    
    model = models.Model(inputs=[text_input, image_input], outputs=output)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

if __name__ == "__main__":
    model = build_multimodal_model()
    model.summary()
