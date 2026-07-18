from src.pdf_loader import extract_text
from src.text_cleaner import clean_text


pdf_text = extract_text("sample.pdf")

cleaned_text = clean_text(pdf_text)

print(cleaned_text[:1000])