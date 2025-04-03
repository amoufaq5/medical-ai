# dataset/dataset_builder.py

import pandas as pd

def build_dataset():
    # Create a sample dataset for common diseases
    data = {
        "disease": [
            "pneumonia", "asthma", "CVD", "common cold", 
            "flu", "covid", "bronchitis", "influenza"
        ],
        "overview": [
            "Inflammation of the lungs caused by infection.",
            "Chronic inflammatory disease of the airways.",
            "A range of diseases affecting the heart and blood vessels.",
            "Viral infection causing sneezing and coughing.",
            "Respiratory illness with fever, body aches, and cough.",
            "Infectious disease caused by coronavirus.",
            "Inflammation of the bronchial tubes.",
            "Seasonal respiratory illness similar to the flu."
        ],
        "symptoms": [
            "Cough, fever, difficulty breathing",
            "Wheezing, shortness of breath, chest tightness",
            "Chest pain, shortness of breath, fatigue",
            "Sneezing, runny nose, sore throat",
            "Fever, cough, muscle aches",
            "Fever, cough, loss of taste/smell",
            "Cough, mucus production, fatigue",
            "Fever, cough, sore throat"
        ],
        "otc_drug": [
            "Acetaminophen, ibuprofen",
            "Inhalers, bronchodilators",
            "Aspirin, beta-blockers",
            "Decongestants, antihistamines",
            "Antiviral, pain relievers",
            "Symptomatic relief drugs",
            "Cough suppressants, expectorants",
            "Antiviral, pain relievers"
        ]
    }
    
    df = pd.DataFrame(data)
    df.to_csv("dataset/data.csv", index=False)
    print("Dataset built and saved to dataset/data.csv")

if __name__ == "__main__":
    build_dataset()
