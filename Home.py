import streamlit as st
from components import show_footer

def load_home_page():
    st.title("👋 Welcome to DiaWatch")

    st.markdown("""
        **DiaWatch** helps you assess your diabetes risk using AI.  
        Just enter your health details and receive personalized results and lifestyle tips.

        ---
        ✅ AI-Powered  
        📖 Educational  
        🧠 Easy to Use
    """)

    st.image(
        "https://cdn.pixabay.com/photo/2017/08/30/07/52/blood-sugar-2690963_960_720.jpg",
        use_column_width=True,
        caption="Track your health with DiaWatch"
    )

    st.markdown("### 🚀 What would you like to do?")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🧮 Check My Risk"):
            st.session_state["page"] = "Risk Checker"

    with col2:
        if st.button("📖 Read Health Articles"):
            st.session_state["page"] = "Education"

    show_footer()
