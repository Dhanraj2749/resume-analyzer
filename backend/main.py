from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from groq import Groq
from dotenv import load_dotenv
import fitz
import json
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

@app.post("/analyze")
async def analyze_resume(file: UploadFile = File(...)):
    pdf_bytes = await file.read()
    resume_text = extract_text_from_pdf(pdf_bytes)

    if not resume_text.strip():
        return {"error": "Could not extract text from PDF"}

    prompt = """You are a resume analyzer. Respond with ONLY a JSON object, no other text.

Analyze this resume and return ONLY this JSON:
{
  "overall_score": <number 1-100>,
  "summary": "<2 sentence summary>",
  "strengths": ["<strength 1>", "<strength 2>", "<strength 3>"],
  "weaknesses": ["<weakness 1>", "<weakness 2>", "<weakness 3>"],
  "improvements": ["<tip 1>", "<tip 2>", "<tip 3>"],
  "sections": {
    "experience": <score 1-10>,
    "skills": <score 1-10>,
    "education": <score 1-10>,
    "formatting": <score 1-10>
  }
}

Resume:
""" + resume_text[:3000]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    raw = response.choices[0].message.content.strip()

    if "```json" in raw:
        raw = raw.split("```json")[1].split("```")[0].strip()
    elif "```" in raw:
        raw = raw.split("```")[1].split("```")[0].strip()

    start = raw.find("{")
    end = raw.rfind("}") + 1
    if start == -1 or end == 0:
        return {"error": "AI did not return valid JSON"}

    raw = raw[start:end]
    result = json.loads(raw)
    return result