import re

abstractpattern = r"ABSTRACT"
intropattern = r"Introduction"

with open('output_text.txt', 'r') as file:
    papertext = file.read()

abstract_match = re.search(abstractpattern, papertext)
intromatch = re.search(intropattern, papertext)

if abstract_match and intromatch:
    abstract_start = abstract_match.end()
    introstart = intromatch.start()
    extracted_content = papertext[abstract_start:introstart]
    print(extracted_content)
else:
    print("Abstract and/or Introduction not found in the text.")
