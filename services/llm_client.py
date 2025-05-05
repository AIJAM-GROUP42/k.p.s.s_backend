import google.generativeai as genai
from decouple import config

genai.configure(api_key=config("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def generate_lesson_content(topic: str) -> tuple[str, str]:
    prompt = f"""
    Konu: {topic}

    1. Bu konunun sade ve anlaşılır bir konu anlatımını yaz.
    2. Ayrıca bu konu için bir ezberleme yöntemi (örneğin: hafıza tekniği, akrostiş veya anahtar kelime) öner.

    Lütfen şu formatta döndür:

    KONUYU ANLAT:
    ...
    EZBERLEME YÖNTEMİ:
    ...
    """

    response = model.generate_content(prompt)
    text = response.text

    split = text.split("EZBERLEME YÖNTEMİ:")
    content = split[0].replace("KONUYU ANLAT:", "").strip()
    memory_tip = split[1].strip() if len(split) > 1 else ""

    return content, memory_tip
