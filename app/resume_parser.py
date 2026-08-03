import fitz  # PyMuPDF

# Path to your PDF resume
pdf_path = pdf_path = "data/resumes/Sonica Balakrishnan Resume 1.pdf"

# Open the PDF
document = fitz.open(pdf_path)

# Read every page
for page_number, page in enumerate(document, start=1):
    print(f"\n----- Page {page_number} -----\n")
    text = page.get_text()
    print(text)

document.close()