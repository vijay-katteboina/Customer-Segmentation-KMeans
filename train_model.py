"""
==========================================================
Customer Segmentation using K-Means Clustering

Author  : Vijay Katteboina
Course  : Master of Computer Applications (MCA)
College : Loyola Academy Degree & PG College

Description:
This program trains a K-Means Clustering model using the
Mall Customer Segmentation Dataset. It performs data
preprocessing, feature scaling, determines the optimal
number of clusters using the Elbow Method, trains the
final model, and saves the trained model files.
==========================================================
"""

import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

# Load Dataset
df = pd.read_csv("dataset/Mall_Customers.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Remove CustomerID
df = df.drop("CustomerID", axis=1)

# Encode Gender
encoder = LabelEncoder()
df["Gender"] = encoder.fit_transform(df["Gender"])

# Feature Scaling
scaler = StandardScaler()
X = scaler.fit_transform(df)

# Elbow Method
wcss = []

for i in range(1, 11):
    model = KMeans(
        n_clusters=i,
        random_state=42,
        n_init=10
    )
    model.fit(X)
    wcss.append(model.inertia_)

plt.figure(figsize=(8,5))
plt.plot(range(1,11), wcss, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.grid(True)
plt.savefig("elbow_method.png")
plt.show()

# Final Model
kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

kmeans.fit(X)

# Save Model
joblib.dump(kmeans, "kmeans_model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(encoder, "encoder.pkl")

print("\nModel Saved Successfully!")