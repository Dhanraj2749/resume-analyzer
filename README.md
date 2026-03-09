\# 🧠 AI Resume Analyzer



An AI-powered resume analyzer built with FastAPI and Groq that provides instant feedback on your resume.



\## ✨ Features



\- 📄 Upload any PDF resume

\-  AI-powered analysis using Groq (LLaMA 3.3)

\-  Overall score out of 100

\-  Strengths, weaknesses \& improvement tips

\-  Section scores for Experience, Skills, Education \& Formatting



\##  Tech Stack



\- \*\*Frontend:\*\* HTML, CSS, JavaScript

\- \*\*Backend:\*\* Python, FastAPI

\- \*\*AI:\*\* Groq API (LLaMA 3.3 70B)

\- \*\*PDF Parsing:\*\* PyMuPDF



\##  Getting Started



\### 1. Clone the repository

```bash

git clone https://github.com/Dhanraj2749/resume-analyzer.git

cd resume-analyzer

```



\### 2. Install dependencies

```bash

pip install fastapi uvicorn groq pymupdf python-multipart python-dotenv

```



\### 3. Set up environment variables

Create a `.env` file in the `backend` folder:

```

GROQ\_API\_KEY=your\_groq\_api\_key\_here

```



\### 4. Run the backend

```bash

cd backend

python -m uvicorn main:app --reload

```



\### 5. Run the frontend

```bash

cd frontend

python -m http.server 3000

```



\### 6. Open in browser

```

http://localhost:3000

```



\##  Security

\- API keys are stored in `.env` file

\- `.env` is excluded from version control via `.gitignore`



\##  License

MIT License

