# PDF Workflow Project

This project is set up for PDF script execution using `pypdf` and `pymupdf`.

## Setup
- Python 3.14.2
- Virtual environment: `venv`
- Libraries: `pypdf`, `pymupdf`

## CRUD Operations
The project now includes basic CRUD operations for PDF files in `pdf_crud.py`:
- **Create**: Generate a new PDF with text content.
- **Read**: Extract text and metadata from a PDF.
- **Update**: Modify PDF metadata (e.g., Title).
- **Delete**: Remove specific pages from a PDF.

## Usage
Activate the virtual environment:
```powershell
.\venv\Scripts\activate
```

Run the demonstration script:
```powershell
python main.py
```
