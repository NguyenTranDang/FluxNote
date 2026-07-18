from pypdf import PdfReader

def extract_text(path):
    reader = PdfReader(path)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


if __name__ == "__main__":
    content = extract_text("sample.pdf")
    print(content[:1000])