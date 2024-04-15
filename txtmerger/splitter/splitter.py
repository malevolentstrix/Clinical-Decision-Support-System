input_filename = "./outputwords.txt"
output_folder = "./splitted_files/"

chunk_size = 50000
chunk_number = 1

with open(input_filename, 'r') as infile:
    while True:
        chunk = infile.read(chunk_size)
        if not chunk:
            break
        output_filename = f"{output_folder}chunk_{chunk_number}.txt"
        with open(output_filename, 'w') as outfile:
            outfile.write(chunk)
        chunk_number += 1
