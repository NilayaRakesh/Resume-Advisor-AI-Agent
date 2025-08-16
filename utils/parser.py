def extract_text_from_pdf(path: str) -> str:
    from PyPDF2 import PdfReader

    reader = PdfReader(path)
    text: str = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text