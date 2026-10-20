import pdf_crud
import os

def main():
    test_file = "test_crud.pdf"
    
    print("--- 1. CREATE ---")
    pdf_crud.create_pdf(test_file, "Page 1: Initial Content")
    
    # Adding another page to test deletion later
    import pymupdf
    doc = pymupdf.open(test_file)
    page = doc.new_page()
    page.insert_text((50, 50), "Page 2: To be deleted")
    
    temp_file = test_file + ".tmp"
    doc.save(temp_file)
    doc.close()
    if os.path.exists(test_file):
        os.remove(test_file)
    os.rename(temp_file, test_file)
    print("Added a second page for testing.")

    print("\n--- 2. READ ---")
    data = pdf_crud.read_pdf(test_file)
    print(f"Content: {data['text'].strip()}")
    print(f"Metadata: {data['metadata']}")

    print("\n--- 3. UPDATE (Metadata) ---")
    pdf_crud.update_pdf_metadata(test_file, "New PDF Title")
    data = pdf_crud.read_pdf(test_file)
    print(f"Updated Title: {data['metadata'].get('title')}")

    print("\n--- 4. DELETE (Page) ---")
    # Let's see page count before
    doc = pymupdf.open(test_file)
    print(f"Pages before deletion: {len(doc)}")
    doc.close()
    
    pdf_crud.delete_pdf_page(test_file, 1) # Delete second page
    
    # Let's see page count after
    doc = pymupdf.open(test_file)
    print(f"Pages after deletion: {len(doc)}")
    doc.close()

    print("\nCRUD operations demo completed.")

if __name__ == "__main__":
    main()
