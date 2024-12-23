import PyPDF2

# Open the PDF file
a = PyPDF2.PdfReader("hallticket.pdf")
print(a.metadata)

# Initialize an empty string to store the extracted text
extracted_text = ""

# Loop through the first 10 pages and extract text
for i in range(0, 2):  # Pages are 0-indexed in PyPDF2
    extracted_text += a.pages[i].extract_text()

# Write the extracted text to a file
with open("text.txt", "w") as f:
    f.write(extracted_text)
