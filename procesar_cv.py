from pathlib import Path
from pypdf import PdfReader

def leer_cv():
    # Ruta donde guardaste tu PDF en la carpeta docs
    docs_path = Path("docs")
    pdf_files = list(docs_path.glob("*.pdf"))
    
    if not pdf_files:
        print("No se encontró ningún archivo PDF en la carpeta docs.")
        return ""
    
    # Toma el primer PDF que encuentre (tu CV)
    cv_file = pdf_files[0]
    print(f"Leyendo CV desde: {cv_file.name}")
    
    reader = PdfReader(cv_file)
    texto_cv = ""
    for page in reader.pages:
        texto_cv += page.extract_text() + "\n"
        
    return texto_cv

if __name__ == "__main__":
    cv_texto = leer_cv()
    print("¡CV leído con éxito! Longitud del texto:", len(cv_texto))