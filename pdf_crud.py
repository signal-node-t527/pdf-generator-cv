import pymupdf # PyMuPDF
import os

def create_pdf(file_path, content="Hello, this is a new PDF!"):
    """Create a new PDF with the given content."""
    doc = pymupdf.open()
    page = doc.new_page()
    page.insert_text((50, 50), content)
    doc.save(file_path)
    doc.close()
    print(f"Created: {file_path}")

def read_pdf(file_path):
    """Read and return text content and metadata from the PDF."""
    doc = pymupdf.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    metadata = doc.metadata
    doc.close()
    return {"text": text, "metadata": metadata}

def update_pdf_metadata(file_path, new_title):
    """Update the title in the PDF metadata."""
    doc = pymupdf.open(file_path)
    metadata = doc.metadata
    metadata["title"] = new_title
    doc.set_metadata(metadata)
    
    # Using a temporary file to avoid incremental write issues
    temp_path = file_path + ".tmp"
    doc.save(temp_path)
    doc.close()
    if os.path.exists(file_path):
        os.remove(file_path)
    os.rename(temp_path, file_path)
    print(f"Updated metadata for: {file_path}")

def delete_pdf_page(file_path, page_number=0):
    """Delete a specific page from the PDF."""
    doc = pymupdf.open(file_path)
    if page_number < len(doc):
        doc.delete_page(page_number)
        temp_path = file_path + ".tmp"
        doc.save(temp_path)
        doc.close()
        if os.path.exists(file_path):
            os.remove(file_path)
        os.rename(temp_path, file_path)
        print(f"Deleted page {page_number} from: {file_path}")
    else:
        doc.close()
        print(f"Error: Page {page_number} out of range.")
