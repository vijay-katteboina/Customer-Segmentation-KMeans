"""
==========================================================
Customer Segmentation using K-Means Clustering

Author  : Vijay Katteboina
Course  : Master of Computer Applications (MCA)
College : Loyola Academy Degree & PG College

Description:
This module loads the trained K-Means model and predicts
the customer cluster based on user input.
==========================================================
"""

# ==========================================================
# Import Required Libraries
# ==========================================================

import os
import joblib
import numpy as np

# ==========================================================
# Get Current Project Directory
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ==========================================================
# Load Saved Model Files
# ==========================================================

print("Loading Trained Model...")

model = joblib.load(os.path.join(BASE_DIR, "kmeans_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))
encoder = joblib.load(os.path.join(BASE_DIR, "encoder.pkl"))

print("Model Loaded Successfully!")

# ==========================================================
# Prediction Function
# ==========================================================

def predict_customer(gender, age, income, score):
    """
    Predict customer cluster using the trained K-Means model.

    Parameters:
        gender (str) : Male or Female
        age (int) : Customer Age
        income (int) : Annual Income
        score (int) : Spending Score

    Returns:
        int : Predicted Cluster Number
    """

    # Convert Gender into Numeric Value
    gender_encoded = encoder.transform([gender])[0]

    # Create Feature Array
    customer_data = np.array([
        [gender_encoded, age, income, score]
    ])

    # Scale Input Data
    customer_data = scaler.transform(customer_data)

    # Predict Cluster
    cluster = model.predict(customer_data)

    return int(cluster[0])

# ==========================================================
# Test Prediction
# ==========================================================

if __name__ == "__main__":

    print("\nTesting Prediction...\n")

    test_cluster = predict_customer(
        "Male",
        25,
        40,
        60
    )

    print(f"Predicted Cluster : {test_cluster}")