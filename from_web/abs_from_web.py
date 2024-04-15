import csv
import requests

def download_page(url, filename):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {url}")
        else:
            print(f"Failed to download: {url} (Status code: {response.status_code})")
    except Exception as e:
        print(f"Error while downloading: {url}\n{str(e)}")

# Reading CSV file with links
csv_file = './researchlinks.csv'  
output_directory = 'downloaded_pages/'  

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        link = row[0]
        filename = output_directory + link.split('/')[-1]  
        download_page(link, filename)
