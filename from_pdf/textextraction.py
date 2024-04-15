import os
import PyPDF2

def extract_abstract(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        abstract = ""
        start_extraction = False

        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text = page.extract_text()
            for i in text:
                if i == "Introduction":
                    break

                if "Abstract" == i:
                    start_extraction = True
                    # Finding the index of "Abstract" and extract text after it
                    abstract += text[text.index("Abstract") + len("Abstract"):]

                if start_extraction:
                    abstract += text

        return abstract.strip()  

# Create a directory to store the extracted abstracts
output_directory = "extracted_abstracts"
os.makedirs(output_directory, exist_ok=True)

# Get a list of PDF files in the "papers" folder
pdf_folder = "./papers"
pdf_files = [file for file in os.listdir(pdf_folder) if file.endswith(".pdf")]

output_file_path = os.path.join(output_directory, "extracted_abstracts.txt")

with open(output_file_path, 'w') as output_file:
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_folder, pdf_file)
        abstract_text = extract_abstract(pdf_path)
        
        output_file.write("\n\n" + abstract_text + "\n\n" + "-" * 40 + "\n")
        
print("Abstracts extracted and saved to", output_file_path)
