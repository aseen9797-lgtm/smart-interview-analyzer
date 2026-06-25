import pdfplumber

with pdfplumber.open(r"C:\Users\aseen\Downloads\Aseens resume.pdf") as pdf:
    print("Pages:", len(pdf.pages))

    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()
        print("Page text:", page_text)
        text += str(page_text)

print(text) 