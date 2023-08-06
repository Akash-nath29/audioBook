import fitz
doc = fitz.open('books/Rich_Dad_Poor_Dad.pdf')
text = ""
for page in doc:
    text+=page.get_text()
print(text)
