📚 AI Study Assistant — GenAI Capstone Project

🧩 1. Problem Statement
Students often work with large volumes of study material in different formats—PDFs, Word files, PowerPoint slides, Excel sheets, and web articles.


Manually reading, summarizing, and preparing study resources like quizzes or flashcards is time-consuming and inefficient.

The challenge is to build an AI-powered agent that can:

->Understand and extract meaningful content from multiple file formats

->Summarize complex documents

->Generate quizzes and flashcards using structured output

->Create a personalized study plan

->Provide an easy-to-use interface

This project solves the problem by integrating Google Gemini and a multi-format text extraction system inside an intuitive Streamlit web application.

🛠 2. Solution Overview

We developed an AI Study Assistant capable of:

->Uploading and reading multiple file formats:
PDF

DOCX

PPTX

XLSX

TXT

Web URLs

->Extracting relevant text

Using PyPDF2, python-docx, openpyxl, python-pptx, and BeautifulSoup.

->Generating study resources automatically:

Concise summaries

Multiple-choice quizzes (MCQs)

Flashcards

7-day study plans

->Using Gemini 2.5 Flash for:

Natural language understanding

Reasoning

Structured output generation

Educational content generation

->Presenting everything in a clean Streamlit UI with:
Tabs

Interactive quiz evaluation

Expandable flashcards

Dynamic content rendering

This end-to-end system provides a smart, automated study workflow powered by GenAI.


🏗 3. System Architecture

![sysarki](https://github.com/user-attachments/assets/5a5c68d4-2b7d-40bc-8bb5-0d6af249e57d)

🪄 4. Key Concepts Used :

1) GenAI Model Usage
Google Gemini 2.5 Flash
GenerateContent API with structured schemas
Multi-task prompting
Educational content generation

2) Agent Design Principles
Modular architecture
Task-specific functions
Clean separation: extraction → processing → AI → UI

3) Structured Output
Gemini JSON schema for:
Quiz questions
Flashcards
Reliable parsing inside Streamlit

4) Multimodal / Multi-format Processing

The agent handles:
Text documents
Presentations
Spreadsheets
Web content

5) User Interaction Flow
Upload → Extract → Generate → Display → Evaluate

📦 5. Requirements

streamlit
python-dotenv
google-genai

PyPDF2
python-docx
openpyxl
python-pptx

requests
beautifulsoup4

Install all dependencies using the below command:

pip install -r requirements.txt

▶ 6. How to Run the Project:

1. Clone the repository:

git clone https://github.com/maddy-madhan-75/Study_Assistant_Web_Application.git
cd Study_Assistant_Web_Application

2. Create and activate a virtual environment:

For Windows:

python -m venv venv
venv\Scripts\activate

For Mac/Linux:

python3 -m venv venv
source venv/bin/activate

3. Install dependencies:

pip install -r requirements.txt

4. Set your Gemini API key:

Create a .env file:

GEMINI_API_KEY=your_api_key_here

5. Run the Streamlit app:

streamlit run main.py

The app will open in your browser.

🖼 7. Screenshots

Home Screen

![g1](https://github.com/user-attachments/assets/064dbb95-6dd6-4e8d-814c-5ac6632bbbb9)

Generated Summary

![g2](https://github.com/user-attachments/assets/66be30c7-1fe2-471d-9564-71cf273eb213)

Generated Quiz

![g3](https://github.com/user-attachments/assets/c1781d80-8ba8-4492-a7bc-7252ceae1319)

Flashcards

![g4](https://github.com/user-attachments/assets/62e1b41e-250a-4916-b963-ab3c5f36c6e4)

Study Plan

![g5](https://github.com/user-attachments/assets/a58aeb89-eafa-492c-9a3f-9ac2cbd16644)


🏁 8. Conclusion

This project demonstrates how GenAI can deeply transform education by automating content understanding and study material generation.
The Study Assistant Agent:
Handles multi-format documents
Extracts meaningful content
Uses Gemini 2.5 Flash for structured reasoning
Generates practical study aids
Presents everything in a usable, clean UI
It showcases end-to-end GenAI agent development, integrating document parsing, structured outputs, and real-time interaction
