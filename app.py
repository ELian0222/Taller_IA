from flask import Flask, render_template, request, jsonify
from pathlib import Path
from pypdf import PdfReader
import ollama

app = Flask(__name__, template_folder='.')

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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/preguntar', methods=['POST'])
def preguntar():
    data = request.get_json()
    pregunta = data.get('pregunta', '')
    
    cv_texto = leer_cv()
    if not cv_texto:
        return jsonify({'respuesta': 'No se encontró el CV en la carpeta docs.'})

    prompt = f"""
    Eres un asistente virtual experto que responde preguntas sobre la siguiente persona basándote únicamente en su currículum.
    Ten en cuenta que estamos en el año 2026 para calcular cualquier edad o duración si es necesario.
    
    Currículum:
    {cv_texto}
    
    Pregunta: {pregunta}
    
    Responde de forma clara, profesional y amable en español. Si la respuesta no está en el currículum, di amablemente que no tienes esa información.
    """

    try:
        response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
        respuesta_ia = response['message']['content']
    except Exception as e:
        respuesta_ia = f"Error al conectar con Ollama: {str(e)}"

    return jsonify({'respuesta': respuesta_ia})

if __name__ == '__main__':
    print("Servidor web iniciado en http://127.0.0.1:5000")
    app.run(debug=True)