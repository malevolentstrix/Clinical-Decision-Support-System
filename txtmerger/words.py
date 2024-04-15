import re

# Path to the input file
input_file = './output.txt'

# Path to the output file
output_file = './outputwords.txt'

# Regular expression to match alphabetical words
pattern = re.compile(r'\b[a-zA-Z]+\b')

# Open the input file for reading and the output file for writing
with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
    # Iterate over each line in the input file
    for line in input_f:
        # Find all alphabetical words in the line
        words = pattern.findall(line)
        # Write the words to the output file, separated by spaces
        if words != []:
            print(words)
            output_f.write(' '.join(words) + '\n')
