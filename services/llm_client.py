import google.generativeai as genai
from decouple import config
import json
import re

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

def generate_quiz(topic: str):
    prompt = f"""
    "{topic}" konusunda 5 adet çoktan seçmeli soru üret.
    Her soruda:
    - 1 doğru cevap ve 3 yanlış cevap olacak (toplam 4 şık).
    - Şıkları karışık sırada ver.
    - Doğrudan JSON formatında, herhangi bir açıklama eklemeden dön. Başka metin yazma, sadece JSON ver.

    Örnek format:
    [
      {{
        "question": "Soru metni",
        "options": ["şık A", "şık B", "şık C", "şık D"],
        "answer_index": 2
      }},
      ...
    ]
    """

    response = model.generate_content(prompt)
    raw_text = response.text.strip()
    
    try:
        # İlk olarak doğrudan JSON olarak çözümlemeyi dene
        try:
            quiz_json = json.loads(raw_text)
            return quiz_json
        except json.JSONDecodeError:
            pass
        
        # Markdown code block içinden JSON çıkarma
        json_match = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', raw_text)
        if json_match:
            json_content = json_match.group(1).strip()
            quiz_json = json.loads(json_content)
            return quiz_json
            
        # Son çare: metindeki ilk "[" ve son "]" arasındaki içeriği al
        start_idx = raw_text.find('[')
        end_idx = raw_text.rfind(']') + 1
        
        if start_idx != -1 and end_idx > start_idx:
            json_content = raw_text[start_idx:end_idx]
            quiz_json = json.loads(json_content)
            return quiz_json
        
        raise ValueError("JSON içeriği bulunamadı")

    except Exception as e:
        return {
            "error": "LLM çıktısı işlenemedi",
            "raw": raw_text,
            "exception": str(e)
        }