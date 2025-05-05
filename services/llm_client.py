import os
import google.generativeai as genai
from dotenv import load_dotenv
import json

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-pro")


def generate_llm_content(topic: str, mode: str) -> str:
    """
    Belirtilen konu ve moda göre içerik üretir:
    - mode: 'info' → Konu anlatımı
    - mode: 'memory_tip' → Hafıza tekniği
    """
    if mode == "info":
        prompt = f"{topic} hakkında sade ve öğretici bir konu anlatımı yap."
    elif mode == "memory_tip":
        prompt = f"{topic} konusunu hatırlamaya yardımcı olacak yaratıcı bir hafıza tekniği geliştir."
    else:
        raise ValueError("Geçersiz mode: 'info' veya 'memory_tip' olmalı.")

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print("Gemini info/memory_tip üretim hatası:", e)
        return "İçerik üretilemedi."


def generate_quiz_with_gemini(topic: str) -> list[dict]:
    """
    Belirtilen konuya göre 3 adet çoktan seçmeli quiz sorusu üretir.
    Her soru formatı:
    {
        "question": "...",
        "options": ["A", "B", "C", "D"],
        "answer": "C"
    }
    """
    prompt = f"""
    "{topic}" hakkında 3 adet çoktan seçmeli soru üret.
    Sadece aşağıdaki JSON formatında yanıt ver:

    [
      {{
        "question": "...",
        "options": ["A", "B", "C", "D"],
        "answer": "C"
      }},
      ...
    ]

    Açıklama veya ek metin yazma. Sadece JSON listesi döndür.
    """

    try:
        response = model.generate_content(prompt)
        raw_json = response.text.strip()

        # JSON veriyi ayrıştır
        quiz = json.loads(raw_json)
        return quiz

    except Exception as e:
        print("Gemini quiz üretim hatası:", e)
        return []
