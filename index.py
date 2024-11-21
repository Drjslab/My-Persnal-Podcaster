from utility import PDFExtractor, GenAI, ReadText
from dotenv import load_dotenv
import json
import os 

load_dotenv()

if __name__ == "__main__":

    # Read personality
    reader = ReadText()
    personality = reader.read(path="personality.txt")

    # PDF Reader
    pdf_path = "1706.03762v7.pdf"
    pdf_reader = PDFExtractor()
    text = pdf_reader.extract_text_from_pdf(pdf_path)

    # Generate Podcast
    genAI = GenAI(api_key=os.getenv("OPEN_AI"))
    podCastContent = genAI.generate(prompt=text, system_prompt=personality)
    print("podCastContent", podCastContent)

    # Genreate Audio file
    genAI.textToAudio(text=podCastContent)