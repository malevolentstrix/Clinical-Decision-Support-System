import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""

    try:
        with open(pdf_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            for page in pdf_reader.pages:
                text += page.extract_text()

        return text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

pdf_path = 'test.pdf'

extracted_text = extract_text_from_pdf(pdf_path)

if extracted_text:
    with open('extracted_text.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(extracted_text)
    print("Text extracted and saved to 'extracted_text.txt'")
else:
    print("Text extraction failed.")
