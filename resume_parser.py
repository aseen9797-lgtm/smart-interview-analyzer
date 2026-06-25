import pdfplumber

def extract_resume_text(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        print("Pages:", len(pdf.pages))

        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text
from resume_parser import extract_resume_text

resume_text = extract_resume_text(
    r"C:\Users\aseen\Downloads\Resume_test.pdf"
)

print(resume_text) 