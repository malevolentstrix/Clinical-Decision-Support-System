import os

# Path to the directory containing the text files
directory = '../output_overall/'

# Path to the output file
output_file = './output.txt'

# Open the output file in append mode
with open(output_file, 'a') as output:
    # Iterate over all the files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                output.write(file.read() + '\n')  # Append the file contents to the output file
