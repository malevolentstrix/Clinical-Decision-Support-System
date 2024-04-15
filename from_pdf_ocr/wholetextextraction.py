
from pdf2image import convert_from_path
import pytesseract

# Replace with the path to your PDF file
pdf_file = 'test.pdf'

# Convert the PDF to a list of images
images = convert_from_path(pdf_file)

# Initialize Tesseract with the path to your Tesseract executable (change this path accordingly)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Extract text from each image
extracted_text = ''
for image in images:
    text = pytesseract.image_to_string(image)
    extracted_text += text

# Print the extracted text
print(extracted_text)
