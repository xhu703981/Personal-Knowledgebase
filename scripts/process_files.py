import fitz
from pathlib import Path

RAW_DIR = Path(r"C:\Users\xhu70\Documents\my-wiki\raw")
OUTPUT_DIR = Path(r"C:\Users\xhu70\Documents\my-wiki\wiki")

def process_pdf(pdf_file):
    doc = fitz.open(pdf_file)
    output_file = OUTPUT_DIR / f"{pdf_file.stem}.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        for page in doc:
            text = page.get_text()
            f.write(text)
    
    doc.close()
