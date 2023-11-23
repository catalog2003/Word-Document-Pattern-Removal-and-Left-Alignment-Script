Remove Patterns: It searches for patterns matching the regular expression \b\d+\.\d+\.\d+\.\d+\b (sequences of digits separated by periods) within the document's paragraphs and removes them.

Left Alignment: It sets the alignment of each paragraph to left align (0 corresponds to left alignment).
![Screenshot 2023-11-23 123633](https://github.com/catalog2003/Word-Document-Pattern-Removal-and-Left-Alignment-Script/assets/83747762/a99aa2ed-c0b7-4889-980d-bdc340810949)
![Screenshot 2023-11-23 123657](https://github.com/catalog2003/Word-Document-Pattern-Removal-and-Left-Alignment-Script/assets/83747762/b1ce0a18-0954-4bc5-b24b-6df999687e1f)

# Word Document Pattern Removal and Left Alignment Script

## Overview
This Python script processes Word documents (`.docx` format), removing specified patterns from the paragraphs while preserving formatting. It also left-aligns the remaining text.

## Usage
1. **Requirements:**
   - Python 3.x
   - `python-docx` library (`pip install python-docx`)

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
Install Dependencies:


pip install python-docx
Run the Script:

python script.py
Replace script.py with the actual name of your Python script.

Input and Output:

Place the Word document you want to process in the same directory as the script.
The modified document will be saved as output.docx in the same directory.
Notes
Make sure to test the script on sample documents before using it on important files.
Adjust the regular expression and code as needed based on your specific requirements.
Example

python process_document.py
