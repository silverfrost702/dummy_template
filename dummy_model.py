from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train simple model
clf = RandomForestClassifier()
clf.fit(X, y)

# Make sure models folder exists
os.makedirs("models", exist_ok=True)

# Save dummy model
with open("models/dummy_model.pkl", "wb") as f:
    pickle.dump(clf, f)

print("✅ Dummy model saved at models/dummy_model.pkl")
