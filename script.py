import re
from docx import Document

def remove_patterns_and_left_align(doc):
    pattern = re.compile(r'\b\d+\.\d+\.\d+\.\d+\b')

    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            original_text = run.text
            modified_text = pattern.sub('', original_text)
            run.text = modified_text

        paragraph.alignment = 0  # Left align

# Example usage:
input_document_path = 'input.docx'
output_document_path = 'output.docx'

doc = Document(input_document_path)
remove_patterns_and_left_align(doc)
doc.save(output_document_path)
