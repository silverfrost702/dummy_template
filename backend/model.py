import pickle
import pandas as pd

def load_model(path="models/dummy_model.pkl"):
    with open(path, "rb") as f:
        return pickle.load(f)

def predict(model, data):
    if isinstance(data, pd.DataFrame):
        return model.predict(data)
    elif isinstance(data, list):
        return model.predict(data)
    elif isinstance(data, dict):  # from API
        df = pd.DataFrame([data])
        return model.predict(df)
    else:
        raise ValueError("Unsupported data type")
