import streamlit as st
import spacy
from skills import skills_list
from extractor import extract_resume_text

nlp = spacy.load("en_core_web_sm")

st.title("Resume Skill Analyzer")

uploaded_file = st.file_uploader("Upload Resume")

def extract_skills(text):

    doc = nlp(text.lower())
    found_skills = []

    for token in doc:
        if token.text in skills_list:
            found_skills.append(token.text)

    return list(set(found_skills))


if uploaded_file:

    text = extract_resume_text(uploaded_file)

    skills = extract_skills(text)

    st.subheader("Detected Skills")

    for skill in skills:
        st.write("✔", skill)
