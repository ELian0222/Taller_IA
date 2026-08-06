from pathlib import Path
from pypdf import PdfReader
import ollama

def leer_cv():
    docs_path = Path("docs")
    pdf_files = list(docs_path.glob("*.pdf"))
    if not pdf_files:
        return ""
    reader = PdfReader(pdf_files[0])
    texto_cv = ""
    for page in reader.pages:
        texto_cv += page.extract_text() + "\n"
    return texto_cv

def consultar_asistente(pregunta):
    # 1. Obtenemos el texto de tu CV
    cv_texto = leer_cv()
    if not cv_texto:
        return "No se pudo cargar el CV."

    # 2. Creamos un prompt estructurado para el modelo local (Llama 3)
    prompt = f"""
    Eres un asistente virtual experto que responde preguntas sobre la siguiente persona basándote únicamente en su currículum.
    
    Currículum:
    {cv_texto}
    
    Pregunta: {pregunta}
    
    Responde de forma clara, profesional y amable en español. Si la respuesta no está en el currículum, di amablemente que no tienes esa información.
    """

    # 3. Llamamos a Ollama localmente (asegúrate de tener Ollama abierto en tu PC)
    print("🤖 Consultando a Ollama...")
    response = ollama.chat(model='llama3', messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])

    return response['message']['content']

if __name__ == "__main__":
    # Puedes cambiar la pregunta para probar
    pregunta_usuario = "¿Qué carrera estudia y cuáles son sus principales habilidades o experiencia?"
    print(f"\nPregunta: {pregunta_usuario}\n")
    
    respuesta = consultar_asistente(pregunta_usuario)
    print("Respuesta del Asistente:\n")
    print(respuesta)