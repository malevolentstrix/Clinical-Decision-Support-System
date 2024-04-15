import csv
from selenium import webdriver

def download_page_selenium(url, filename):
    try:
        driver = webdriver.Chrome() 

        driver.get(url)
        html = driver.page_source

        if html:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(html)
            print(f"Downloaded: {url} -> {filename}")
        else:
            print(f"Failed to download: {url}")
    except Exception as e:
        print(f"Error while downloading: {url}\n{str(e)}")
    finally:
        driver.quit()

csv_file = 'researchlinks.csv'  
output_directory = 'downloaded_pages/'  

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    for index, row in enumerate(reader):
        link = row[0]
        filename = f"{output_directory}index_{index}.html"
        download_page_selenium(link, filename)
