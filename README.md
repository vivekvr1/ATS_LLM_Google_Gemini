# Smart Resume Match: Ace the ATS Game!

## Overview

The **Smart Resume Match** project aims to assist job seekers in optimizing their resumes for Applicant Tracking Systems (ATS) by comparing their resume against a given job description. Using advanced AI, this tool evaluates the resume, provides a matching score, identifies missing keywords, and generates a detailed profile summary. This helps users to enhance their resumes, increasing their chances of getting noticed by recruiters.

## Features

- **Upload Resume**: Upload your resume in PDF format.
- **Job Description Input**: Provide the job description for the role you are applying for.
- **AI-Powered Analysis**: Uses Google Generative AI to analyze the resume and job description.
- **Matching Score**: Displays a matching score in both progress bar and percentage format.
- **Missing Keywords**: Lists keywords that are missing from your resume but are present in the job description.
- **Profile Summary**: Provides a detailed summary of your profile highlighting key strengths and areas of improvement.

## Installation

### Prerequisites

- Python 3.7 or higher
- [Streamlit](https://streamlit.io/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [dotenv](https://pypi.org/project/python-dotenv/)
- [Google Generative AI API Key](https://console.cloud.google.com/)

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/smart-resume-match.git
   cd smart-resume-match
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the project root directory.
   - Add your Google API key to the `.env` file:
     ```
     GOOGLE_API_KEY=your_google_api_key
     ```

5. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Open the Application:**
   - After running the application, it will open in your default web browser.

2. **Input Job Description:**
   - Enter the job description for the role you are applying for in the provided text area.

3. **Upload Resume:**
   - Click the "Browse files" button to upload your resume in PDF format.

4. **Submit:**
   - Click the "Submit" button to get the analysis.

5. **View Results:**
   - The matching score will be displayed as a progress bar and percentage.
   - Missing keywords will be listed.
   - A profile summary will be generated to help you understand your strengths and areas of improvement.

## Project Structure

```plaintext
smart-resume-match/
│
├── app.py                # Main application file
├── requirements.txt      # Dependencies
├── .env                  # Environment variables file (to be created)
├── README.md             # Project documentation
└── venv/                 # Virtual environment directory
```

## Code Explanation

### `app.py`

- **Import Statements:**
  - Import necessary libraries such as Streamlit, Google Generative AI, PyPDF2, dotenv, and os.
  
- **Configuration:**
  - Load environment variables and configure the Google Generative AI with the API key.

- **Functions:**
  - `get_gemini_response(prompt)`: Sends a prompt to the Generative AI and returns the response.
  - `get_pdf_text(uploaded_file)`: Extracts text from the uploaded PDF file.
  - `parse_response(response_string)`: Parses the plain response string from the AI to extract match score, missing keywords, and profile summary.
  - `format_response(response)`: Formats and displays the response on the Streamlit app.

- **Streamlit App Layout:**
  - Title and subtitle for the app.
  - Input fields for job description and resume upload.
  - Submit button to trigger the analysis.
  - Display results including match score, missing keywords, and profile summary.

## Contributing

We welcome contributions to improve the **Smart Resume Match** project. If you have any ideas, suggestions, or bug fixes, feel free to submit a pull request or open an issue.

### Steps to Contribute

1. **Fork the repository.**
2. **Create a new branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes.**
4. **Commit your changes:**
   ```bash
   git commit -m 'Add some feature'
   ```
5. **Push to the branch:**
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Create a pull request.**

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

For any questions or suggestions, please contact:
- **Email**: [mayurjadhsvsm@gmail.com](mailto:mayurjadhavsm@gmail.com)
- **GitHub**: [https://github.com/MayurJadhav-1998](https://github.com/MayurJadhav-1998)

---

By using this application, you agree to our terms and conditions. Please ensure your resume does not contain sensitive personal information before uploading.

---

**Smart Resume Match: Ace the ATS Game!** - Boost your chances with a resume that shines!
```
