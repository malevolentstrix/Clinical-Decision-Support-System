import fitz  # PyMuPDF
import re

def extract_abstract(pdf_path):
    abstract = ""
    pdf_document = fitz.open(pdf_path)
    abstract_start = None  # Initialize abstract_start to None

    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        page_text = page.get_text()

        # Define custom regular expressions to find the start and end of the abstract.
        start_pattern = r"^\s*(abstract|summary)\s*$"
        end_pattern = r"^\s*(1\s+introduction|2\s+background|3\s+related work)\s*$"

        if re.search(start_pattern, page_text, re.IGNORECASE):
            abstract_start = page_num + 1
        if re.search(end_pattern, page_text, re.IGNORECASE):
            abstract_end = page_num
            break

    if abstract_start is not None:  # Check if abstract_start is found
        for page_num in range(abstract_start, abstract_end):
            page = pdf_document[page_num]
            page_text = page.get_text()
            abstract += page_text

    return abstract

pdf_path = 'test.pdf'
abstract_text = extract_abstract(pdf_path)
print(abstract_text)
