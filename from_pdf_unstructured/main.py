from langchain_community.document_loaders import UnstructuredPDFLoader
import os

input_folder = 'input_files'
output_folder = 'output_files_unstructured'

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Initialize the PDF loader

# Loop through all PDF files in the input folder
for pdf_file in os.listdir(input_folder):
    if pdf_file.endswith('.pdf'):
        pdf_path = os.path.join(input_folder, pdf_file)
        try:
            # Load the PDF file
            loader = UnstructuredPDFLoader(pdf_path)
            data = loader.load()
        except Exception as e:
            print(f"Error loading {pdf_file}: {e}")
            continue

        # Create a single text file for each PDF
        output_text_file = open(os.path.join(output_folder, f'{pdf_file}.txt'), 'w', encoding='utf-8')

        # Write the extracted text to the output file

        output_text_file.write(str(data[0]) + '\n\n')
            
        output_text_file.close()
        print(f'Text extracted from {pdf_file} and saved to {pdf_file}.txt')
