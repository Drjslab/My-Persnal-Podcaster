import pdfplumber

class PDFExtractor:
    def __init__(self):
        pass  # Initialize any required attributes if needed
    
    @staticmethod
    def extract_text_from_pdf(file_path):
        """
        Extract text from a PDF file.

        Args:
            file_path (str): Path to the PDF file.

        Returns:
            str: Extracted text from the PDF.
        """
        extracted_text = ""
        try:
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    extracted_text += page.extract_text() or ""
        except FileNotFoundError:
            return f"Error: File '{file_path}' not found."
        except Exception as e:
            return f"An error occurred: {e}"

        return extracted_text.strip()

# Example Usage
if __name__ == "__main__":
    pdf_path = "example.pdf"  # Replace with your PDF file path
    pdf_reader = PDFExtractor()
    text = pdf_reader.extract_text_from_pdf(pdf_path)
    print(text)
