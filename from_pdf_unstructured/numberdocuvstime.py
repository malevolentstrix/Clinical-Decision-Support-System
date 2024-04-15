import time
import matplotlib.pyplot as plt
from langchain_community.document_loaders import UnstructuredPDFLoader

# Initialize the PDF loader

# Number of times to process the document
num_runs = 200

# List to store the time taken for each run
times = []

# Load and process the document multiple times
for i in range(1, num_runs + 1):
    start_time = time.time()
    loader = UnstructuredPDFLoader("/home/jithin/fyp/from_pdf_unstructured/TONURSJ-3-33.pdf")
    data = loader.load()
    end_time = time.time()
    times.append((end_time - start_time) * 1000)  # Convert to milliseconds

    if i % 10 == 0:
        print(f"Processed document {i} times")

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(range(10, num_runs + 1, 10), times[9::10], marker='o')
plt.xlabel('Number of Times Document Processed')
plt.ylabel('Time taken (ms)')
plt.title('Document Processing Time vs Number of Times Processed')
plt.grid(True)
plt.show()
