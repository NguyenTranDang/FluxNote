import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)

    text = text.strip()

    return text


if __name__ == "__main__":
    sample = "Hello     world\n\nThis is a test."
    print(clean_text(sample))