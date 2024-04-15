import requests
from pdf2image import convert_from_path
from PIL import Image
from io import BytesIO

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

    # get the recognized text
    extracted_text = result['ParsedResults'][0]['ParsedText']
    return extracted_text

pdf_file = 'test.pdf'

images = convert_from_path(pdf_file)

# Creating a single text file
output_file = open('output_text.txt', 'w', encoding='utf-8')

for i, image in enumerate(images):
    image.save('page_{}.png'.format(i), 'PNG')  # Save each page as a PNG image
    extracted_text = ocr_space_api('page_{}.png'.format(i), api_key)
    
    output_file.write('Page {} Text:\n'.format(i + 1))
    output_file.write(extracted_text + '\n\n')
    
    print('Page {} Text appended to output_text.txt'.format(i + 1))

output_file.close()