# file-converter

A Python file conversion utility that lets users convert documents between multiple formats such as PDF, TXT, DOCX, and CSV. Supports batch conversions, error-handling, and a simple interface for easy use.

## Project Structure

```
file-converter/
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── input/                 # Folder for files to convert
├── output/                # Folder for converted files
├── converters/            # Converter modules
│   ├── __init__.py        # Package initialization
│   ├── base_converter.py  # Abstract base class for all converters
│   ├── csv_converter.py   # CSV file converter
│   ├── pdf_converter.py   # PDF file converter
│   ├── docx_converter.py  # Word document converter
│   └── txt_converter.py   # Text file converter
├── ui/                    # User interface
│   └── gui.py            # GUI implementation
└── utils/                 # Utility functions
    └── file_utils.py     # File handling utilities
```

## Currently Implemented

### Converters

- **CSVConverter**: Converts CSV files to Excel (.xlsx), JSON, HTML, or CSV format
- **PDFConverter**: Converts PDF files to Word (.docx) format
- **DOCXConverter**: Converts Word documents to plain text (.txt) format
- **TXTConverter**: Converts text files to CSV, Excel (.xlsx), or JSON format

### Base Infrastructure

- **BaseConverter**: Abstract base class that all converters inherit from
- **Error Handling**: Try-catch blocks in all converters with informative error messages
- **Input Validation**: File existence checking before conversion
- **File Type Detection**: Automatic detection of output file formats

## Dependencies

The project uses the following Python libraries (see `requirements.txt`):

- **pandas** - Data manipulation and CSV/Excel operations
- **python-docx** - Reading and writing Word documents
- **pdf2docx** - Converting PDF files to Word format
- **openpyxl** - Excel file operations
- **Pillow** - Image processing (for future enhancements)

## Installation

1. Clone the repository
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use

1. Place the file you want to convert in the `input/` folder
2. Specify the input file path and desired output format
3. Run the converter
4. Find the converted file in the `output/` folder

## To Do

- [ ] Complete `main.py` - Main application logic
- [ ] Complete `utils/file_utils.py` - File utility functions
- [ ] Complete `ui/gui.py` - Graphical user interface
