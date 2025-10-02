import streamlit as st
import pandas as pd
from backend.model import load_model, predict
from backend.api_connector import fetch_data

st.set_page_config(page_title="Data Science App Template", layout="wide")

# Sidebar
st.sidebar.title("⚙️ Settings")
mode = st.sidebar.selectbox("Choose Mode:", ["Upload Data", "Use API", "Manual Input"])

st.title("📊 General Data Science App Template")

# Input Section
data = None
if mode == "Upload Data":
    file = st.file_uploader("Upload CSV", type=["csv"])
    if file is not None:
        data = pd.read_csv(file)
        st.write("Uploaded Data:", data.head())
elif mode == "Use API":
    data = fetch_data()
    st.write("API Data:", data)
else:
    user_input = st.text_input("Enter input values (comma-separated, 4 numbers for Iris)")
    if user_input:
        try:
            data = [list(map(float, user_input.split(",")))]
            st.write("Manual Input:", data)
        except:
            st.error("Please enter valid numbers separated by commas.")

# Prediction Section
if st.button("🔮 Predict"):
    model = load_model()
    if data is not None:
        preds = predict(model, data)
        st.success(f"✅ Predictions: {preds}")
    else:
        st.warning("Please provide input data first!")
