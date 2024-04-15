import requests
import os
from pdf2image import convert_from_path
from PIL import Image
from io import BytesIO
from pdf2image.exceptions import PDFPageCountError


# API
api_key = 'K81776874988957'

def ocr_space_api(image_path, api_key):
    image = Image.open(image_path)

    # Convert the PIL Image to bytes
    image_bytes = BytesIO()
    image.save(image_bytes, format='PNG')
    image_bytes.seek(0)

    # Prepare the POST request
    url = 'https://api.ocr.space/parse/image'
    payload = {
        'apikey': api_key,
        'language': 'eng',
    }
    files = {'file': ('image.png', image_bytes)}

    # Send the POST request to the OCR.space API
    response = requests.post(url, data=payload, files=files)
    result = response.json()
    print(response)

    # get the recognized text
    if 'ParsedResults' in result and len(result['ParsedResults']) > 0:
        extracted_text = result['ParsedResults'][0]['ParsedText']
        return extracted_text
    else:
        extracted_text = 'No text extracted'    
    

# Input and output folders
input_folder = 'input_files'
output_folder = 'output_files'
image_folder = 'images'

# Ensure output folders exist
os.makedirs(output_folder, exist_ok=True)
os.makedirs(image_folder, exist_ok=True)

# Loop through all PDF files in the input folder
for pdf_file in os.listdir(input_folder):
    if pdf_file.endswith('.pdf'):
        pdf_path = os.path.join(input_folder, pdf_file)
        try:
            images = convert_from_path(pdf_path)
        except PDFPageCountError as e:
            print(f"Skipping {pdf_file}: {e}")
            continue

        # Create a single text file for each PDF
        output_text_file = open(os.path.join(output_folder, f'{pdf_file}.txt'), 'w', encoding='utf-8')

        for i, image in enumerate(images):
            image_path = os.path.join(image_folder, f'{pdf_file}_page_{i}.png')
            image.save(image_path, 'PNG')  # Save each page as a PNG image
            extracted_text = ocr_space_api(image_path, api_key)
            
            output_text_file.write(f'Page {i + 1} Text:\n')
            if extracted_text is not None:
                output_text_file.write(extracted_text + '\n\n')
            else:
                output_text_file.write('No text extracted\n\n')
            
            print(f'Page {i + 1} Text appended to {pdf_file}.txt')

        output_text_file.close()