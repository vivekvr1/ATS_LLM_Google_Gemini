import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
import json
from dotenv import load_dotenv
from csv import reader

load_dotenv()
genai_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=genai_key)

def get_gemini_response(prompt):
   model=genai.GenerativeModel("gemini-pro")
   repsonse=model.generate_content(prompt)
   return repsonse.text

def get_pdf_text(uploaded_file):
    pdf_reader = pdf.PdfReader(uploaded_file)
    print(pdf_reader.pages)
    text=""
    for page in pdf_reader.pages:
        text+=str(page.extract_text())
    return text

#prompt Template
input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Job description and the resume. You must also provide the list of the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in the with Following Structure: 
"Match": "0.5",
"MissingKeywords": ["keyword1", "keyword2"],
"Profile Summary": "This is a sample profile summary"
"""
#Steamlit App
st.title("Smart Resume Matcher Gen AI")
st.subheader("Boost your chances with a resume that shines!")
jd=st.text_area("Job Description for the Role")
uploaded_file=st.file_uploader("Upload your Resume", type="pdf",help="Upload your Resume here")
submit=st.button("Submit")

def parse_response(response_string):
    """Parses the plain response string and extracts relevant data."""
    try:
        response_data = {}
        lines = response_string.split('\n')
        for line in lines:
            if 'Match' in line:
                response_data['Match'] = line.split(': ')[1].strip().strip('"').strip(',')
            elif 'MissingKeywords' in line:
                keywords = line.split(': ')[1].strip().strip('[]').replace('"', '').split(', ')
                response_data['MissingKeywords'] = keywords
            elif 'Profile Summary' in line:
                response_data['Profile Summary'] = line.split(': ', 1)[1].strip().strip('"')
        return response_data
    except Exception as e:
        print("Error parsing response string:", e)
        return None

def format_response(response):
    """Formats the response into a human-readable and visually appealing structure."""
    if response:
        match = response.get("Match")
        match=match.strip('"')
        missing_keywords = response.get("MissingKeywords", [])
        profile_summary = response.get("Profile Summary", "No summary provided.")

        # Clean and convert match score to a float for the progress bar
        try:
            match_score = float(match)
        except ValueError:
            st.error("Invalid match score value")
            return

        match_percentage = int(match_score * 100)

        col1, col2, col3 = st.columns([1, 1, 2])

        with col1:
            st.markdown("### Match Score")
            st.progress(match_score)
            st.markdown(f"<h1 style='text-align: center;'>{match_percentage}%</h1>", unsafe_allow_html=True)

        with col2:
            st.markdown("### Missing Keywords")
            if missing_keywords:
                for keyword in missing_keywords:
                    st.markdown(f"- {keyword}")
            else:
                st.success("Your resume aligns well with the job description's keywords!")

        with col3:
            st.markdown("### Profile Summary")
            st.markdown(profile_summary)

    else:
        st.error("Failed to parse the response.")

if submit:
    if uploaded_file is not None:
        text=get_pdf_text(uploaded_file)
        
        respone=(get_gemini_response(input_prompt.format(text=text, jd=jd)))
        response_json = parse_response(respone)
        format_response(response_json)

    else:
        st.write("Please upload your Resume")