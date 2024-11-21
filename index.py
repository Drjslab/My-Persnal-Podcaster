from utility import PDFExtractor, GenAI, re
from dotenv import load_dotenv
import json
import os 

load_dotenv()

if __name__ == "__main__":

    reader = ReadText()
    personality = reader.read(path="personality.txt")

    pdf_path = "1706.03762v7.pdf"
    pdf_reader = PDFExtractor()
    genAI = GenAI(api_key=os.getenv("OPEN_AI"))
    text = pdf_reader.extract_text_from_pdf(pdf_path)
    print(text)
