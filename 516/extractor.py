from pdfminer.high_level import extract_text

def extract_resume_text(file):

    if file.name.endswith(".pdf"):
        text = extract_text(file)

    else:
        text = file.read().decode("utf-8")

    return text
