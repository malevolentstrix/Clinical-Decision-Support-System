import os
import time
import subprocess
import matplotlib.pyplot as plt

# Define the original PDF file path
original_pdf_path = "/content/original.pdf"

# Define the output folder
output_folder = "output_files"
os.makedirs(output_folder, exist_ok=True)

# Define the target sizes in KB
target_sizes_kb = list(range(100, 2100, 100))

# List to store the processing times
processing_times = []

# Truncate the original PDF file to create new files of target sizes
for target_size_kb in target_sizes_kb:
    target_size_bytes = target_size_kb * 1024
    truncated_pdf_path = os.path.join(output_folder, f"truncated_{target_size_kb}KB.pdf")
    start_time = time.time()
    subprocess.run(["pdftk", original_pdf_path, "cat", "1-endeast", "output", truncated_pdf_path])
    end_time = time.time()
    processing_times.append((end_time - start_time) * 1000)  # Convert to milliseconds

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(target_sizes_kb, processing_times, marker='o')
plt.xlabel('Target File Size (KB)')
plt.ylabel('Time taken (ms)')
plt.title('Processing Time vs Target File Size')
plt.grid(True)
plt.show()
