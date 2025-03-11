import PyPDF2
import re
import time  # For a slight delay effect in the intro
import sys   # For typewriter effect

def typewriter_effect(text, delay=0.03):
    """Simulates a typewriter effect by printing text character by character."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Newline at the end

def display_intro():
    """Displays a stylized intro message and explanation."""
    print("\n" + "="*60)
    typewriter_effect("Welcome to the PDF Date Extractor!")
    print("="*60)
    time.sleep(0.5)
    typewriter_effect("This tool will dive into your PDF file and pull out entries")
    typewriter_effect("starting with dates in the format MM/DD/YY (e.g., 02/20/25).")
    time.sleep(0.5)
    typewriter_effect("Here’s what’s about to happen:")
    print("  - We’ll open 'example_doc.pdf'.")
    print("  - Scan each page for date entries.")
    print("  - Show you what we find, page by page!")
    print("="*60)
    time.sleep(0.5)

def confirm_ready():
    """Asks the user if they’re ready to proceed."""
    while True:
        typewriter_effect("Are you ready to start? (yes/no): ")
        response = input().strip().lower()
        if response in ["yes", "y"]:
            typewriter_effect("Great! Let’s get started...")
            time.sleep(1)
            return True
        elif response in ["no", "n"]:
            typewriter_effect("Okay, exiting now. See you next time!")
            time.sleep(1)
            sys.exit(0)
        else:
            typewriter_effect("Please type 'yes' or 'no'.")

def extract_text():
    try:
        file_path: str = "example_doc.pdf"
        with open(file_path, 'rb') as file:
            # Create PDF reader
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            print(f"\nTotal pages in the PDF: {num_pages}")
            all_the_text = ""

            # Extract text from each page
            for page_num in range(num_pages):
                print(f"\nProcessing page {page_num + 1}...")
                # Get the page object
                page = pdf_reader.pages[page_num]
                page_text = page.extract_text()
                
                # Print raw text for debugging
                print(f"Raw text from page {page_num + 1}:\n{repr(page_text)}\n{'-'*50}")

                # Regex pattern to match date entries
                pattern = r"\d{2}/\d{2}/\d{2}.*?(?=\d{2}/\d{2}/\d{2}|$)"
                
                # Find all matches
                matches = re.findall(pattern, page_text, re.DOTALL)

                # Append each match to all_the_text 
                if matches:
                    for i, match in enumerate(matches, 1):
                        all_the_text += f"Entry {i} (Page {page_num + 1}):\n{match.strip()}\n{'-'*50}\n"
                else:
                    print(f"No date entries found on page {page_num + 1}")

            # Print the final result
            if all_the_text:
                print("\n" + "="*60)
                typewriter_effect("Here are all the extracted entries:")
                print("="*60)
                print(all_the_text)
            else:
                print("\nNo date entries found in the entire document.")

    except Exception as e:
        print(f"\nOops! Something went wrong: {e}")
        print("Make sure 'example_doc.pdf' exists and is readable!")

if __name__ == "__main__":
    # Run the interactive sequence
    display_intro()
    confirm_ready()
    extract_text()
    print("\n" + "="*60)
    typewriter_effect("All done! Thanks for using the PDF Date Extractor!")
    print("="*60)