import streamlit as st

def show_footer():
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; font-size: 0.9em;'>"
        "© 2025 DiaWatch | Built by Team XYZ | Educational use only."
        "</p>",
        unsafe_allow_html=True
    )



