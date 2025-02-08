import joblib
import os
import numpy as np
import pandas as pd


model_path = "./random_forest.joblib" 

if os.path.exists(model_path):
    model = joblib.load(model_path)
    print("Model loaded successfully!")
    feature_names = ["body temperature", "pulse", "SpO2"]
    example_input = [[5.1, 3.5, 1.4]] 
    example_input = np.array(example_input);
    try:
        prediction = model.predict(example_input)
        print(f"Prediction: {prediction}")
    except Exception as e:
        print(f"Error during prediction: {e}")
else:
    print("Model file not found. Please check the path.")
