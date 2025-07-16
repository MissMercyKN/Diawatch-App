# education.py

import streamlit as st
import os

# Function to load markdown content
def load_article(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "⚠️ Article not found: " + filepath

def app():
    st.title("📚 DiaWatch Health Articles")
    st.markdown("Explore helpful information about diabetes. Click below to read more.")

    # Article list (EDIT ONLY IF YOU CHANGE FILENAMES)
    articles = [
        {
            "title": "📌 Understanding Diabetes",
            "image": "assets/diabetes_basics.jpg",
            "file": "articles/what_is_diabetes.md"
        },
        {
            "title": "🚨 Early Symptoms of Diabetes",
            "image": "assets/symptoms.jpg",
            "file": "articles/symptoms_causes.md"
        },
        {
            "title": "💡 Preventing Type 2 Diabetes",
            "image": "assets/prevention.jpg",
            "file": "articles/prevention_tips.md"
        },
        {
            "title": "🧪 Importance of Early Screening",
            "image": "assets/screening.jpg",
            "file": "articles/importance_screening.md"
        }
    ]

    for article in articles:
        with st.container():
            st.markdown("---")
            col1, col2 = st.columns([1, 4])

            with col1:
                if os.path.exists(article["image"]):
                    st.image(article["image"], width=100)
                else:
                    st.error(f"Image not found: {article['image']}")

            with col2:
                st.subheader(article["title"])
                with st.expander("📖 Read More"):
                    content = load_article(article["file"])
                    st.markdown(content, unsafe_allow_html=True)

# Only runs this page if it's the main script
if __name__ == "__main__":
    app()
