import fitz

from information_extractor import extract_email, extract_phone


pdf_path = "data/resumes/Sonica Balakrishnan Resume 1.pdf"

document = fitz.open(pdf_path)

text = ""

for page in document:
    text += page.get_text()

document.close()
print("----- EMAIL -----")
print(extract_email(text))

print("\n----- PHONE -----")
print(extract_phone(text))