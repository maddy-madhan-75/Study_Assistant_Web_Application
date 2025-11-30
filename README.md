📚 Study Assistant — AI-Powered Learning Companion

A Streamlit application that extracts text from uploaded files or URLs and uses Google Gemini to generate:

->Concise summaries

->Multiple-choice quizzes

->Flashcards

->7-day study plans

Designed for students and educators who want fast and intelligent learning support.

🚀 Features
1. Multi-format File Support

Upload widely used study materials:

TXT

PDF

DOCX

XLSX

PPTX

Or provide a URL, and the system extracts meaningful text from the webpage.

2. AI-Generated Outputs (Powered by Gemini 2.5 Flash)

Summary — clean, structured markdown summarization

Quiz — 5 structured MCQs with answers & explanations

Flashcards — 10 term–definition pairs

Study Plan — custom 7-day structured learning schedule

3. Modern, Interactive UI

Built entirely using Streamlit

Tabs for each feature

Real-time feedback

Session-based grading and quiz interactions

🧠 System Architecture
+-------------+
|  User Input |
+-------------+
      |
      v
+-----------------------+
| File / URL Extraction |
|  - PDF (PyPDF2)       |
|  - DOCX (python-docx) |
|  - XLSX (openpyxl)    |
|  - PPTX (python-pptx) |
|  - URL (BeautifulSoup)|
+-----------------------+
      |
      v
+-----------------------+
|  Unified Text Router  |
+-----------------------+
      |
      v
+------------------------------+
| Gemini 2.5 Flash Generation  |
|  - Summary                   |
|  - Quiz (Structured Output)  |
|  - Flashcards                |
|  - Study Plan                |
+------------------------------+
      |
      v
+-----------------------+
| Streamlit UI Renderer |
+-----------------------+

🛠️ Technologies Used
Backend / Logic

Python 3.10+

Google Gemini (google-genai)

Text processing libraries:

PyPDF2

python-docx

openpyxl

python-pptx

beautifulsoup4

requests

Frontend

Streamlit

HTML/CSS rendering inside Streamlit

Session state for interaction handling

📦 Installation
1. Clone the repository
git clone <your-repo-url>
cd study_assistant

2. Create a virtual environment
python -m venv venv

3. Activate the environment

If Windows

venv\Scripts\activate


If Mac/Linux

source venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

5. Set your Gemini API Key

Create a .env file:

GEMINI_API_KEY=your_api_key_here

▶️ Running the App
streamlit run main.py


Open the link Streamlit provides in your browser.

📁 Project Structure
study_assistant/
│
├── main.py                 # Streamlit application
├── requirements.txt        # Dependencies
├── lib/
│   └── quizzing_engine.py  # Structured Quiz/Flashcard models
├── README.md               # Documentation
└── .env                    # Environment variables (not committed)

✨ Key Functions Overview
Text Extraction

PDFs → PyPDF2

Word files → python-docx

Excel → openpyxl

PowerPoint → python-pptx

Webpages → requests + BeautifulSoup

AI Processing

Each of these uses Gemini:

generate_summary()

generate_quiz()

generate_flashcards()

generate_study_plan()

Structured Outputs

Quiz and flashcards use Gemini JSON-mode or schema-based responses to ensure consistent output.

🧪 Example Outputs
Summary (Sample)
## Key Concepts
- ...
- ...

Quiz (Sample)
Q1. What is ...?
A) ...
B) ...
Correct: B

Flashcards (Sample)
Front: Term A
Back: Definition A

Study Plan (Sample)
Day 1 — Read primary notes
Day 2 — Build flashcards
Day 3 — Solve practice questions
...

🧩 Known Limitations

Model output may vary; fallback logic handles unexpected structures

Very large PDF/URL content may be slower to process

The app does not currently support image OCR

🔮 Future Improvements

Add embeddings for semantic search

Add long-context Gemini models (e.g., Flash Thinking)

Save and re-load generated quizzes

Support PDF tables extraction

Add RAG-based augmentation

Deploy via Streamlit Cloud or Render

🏁 Conclusion

The AI Study Assistant is a flexible and powerful tool for transforming study materials into structured, interactive learning assets. It demonstrates:

Modern GenAI skills

Multi-format file processing

Structured output design

Real-time UI development with Streamlit

Perfect for learning, education workflows, and rapid prototyping of AI-powered study tools.