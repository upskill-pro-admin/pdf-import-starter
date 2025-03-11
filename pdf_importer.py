import PyPDF2

import PyPDF2
import re

def extract_text():
    try:
        file_path: str = "example_doc.pdf"
        with open(file_path, 'rb') as file:
            # Create PDF reader
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            print(f"Total pages: {num_pages}")
            all_the_text = ""

            # Extract text from each page
            for page_num in range(num_pages):
                print(f"Processing page {page_num + 1}")
                # Get the page object
                page = pdf_reader.pages[page_num]
                page_text = page.extract_text()
                
                # Print raw text for debugging
                print(f"Raw text from page {page_num + 1}:\n{repr(page_text)}\n{'='*50}")

                # Regex pattern to match date entries (adjusted)
                pattern = r"\d{2}/\d{2}/\d{2}.*?(?=\d{2}/\d{2}/\d{2}|$)"
                
                # Find all matches
                matches = re.findall(pattern, page_text, re.DOTALL)

                # Append each match to all_the_text 
                if matches:
                    for i, match in enumerate(matches, 1):
                        all_the_text += f"Entry {i} (Page {page_num + 1}):\n{match.strip()}\n{'-'*50}\n"
                else:
                    print(f"No matches found on page {page_num + 1}")

            # Print the final result
            if all_the_text:
                print("Extracted Entries:\n", all_the_text)
            else:
                print("No entries found in the entire document.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    extract_text()