import streamlit as st
from model import predict_diabetes
from components import show_footer

def load_results_page():
    st.title("🔍 Your Diabetes Risk Assessment")

    if "user_input" not in st.session_state:
        st.warning("⚠️ No data submitted yet. Please use the Risk Checker form.")
        return

    input_data = st.session_state["user_input"]
    risk_level, confidence = predict_diabetes(input_data)

    st.subheader("🧠 AI Prediction Results")
    st.success(f"**Risk Level:** {risk_level}")
    st.info(f"**Prediction Confidence:** {round(confidence * 100, 2)}%")

    st.subheader("📋 Lifestyle Recommendations")
    if risk_level == "Low":
        st.markdown("✅ Keep up your healthy lifestyle. Continue exercising and eating well.")
    elif risk_level == "Medium":
        st.markdown("⚠️ Moderate risk. Improve your diet, increase physical activity, and monitor glucose levels.")
    elif risk_level == "High":
        st.error("❗ High risk detected. Please see a healthcare provider as soon as possible.")
    else:
        st.write("No recommendation available.")

    with st.expander("🔎 Review Your Submitted Info"):
        for key, value in input_data.items():
            st.write(f"**{key}**: {value}")

    show_footer()
