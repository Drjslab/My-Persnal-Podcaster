from utility import PDFExtractor, GenAI, ReadWriteTextFile
from dotenv import load_dotenv
import json
import os 

load_dotenv()

if __name__ == "__main__":

    # Read personality
    print("personality Created.")
    reader = ReadWriteTextFile()
    personality = reader.read(path="personality.txt")

    # PDF Reader
    print("PDF Extacted.")
    pdf_path = "1706.03762v7.pdf"
    pdf_reader = PDFExtractor()
    text = pdf_reader.extract_text_from_pdf(pdf_path)

    # Generate Podcast
    print("Generating podcast.")
    genAI = GenAI(api_key=os.getenv("OPEN_AI"))
    podCastContent = genAI.generate(prompt=text, system_prompt=personality)
    
    print("Save podcast")
    reader.write(content=podCastContent, file_name=f"{pdf_path}.txt")

    # Genreate Audio file
    print("Geneate Audio file.")
    genAI.textToAudio(text=podCastContent , system_prompt=personality, audio_file=f"{pdf_path}.txt")
    print("Program Exit.")