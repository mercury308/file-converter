# CSV Converter module - converts CSV files to other formats

# Import pandas library for working with CSV files 
import pandas as pd

# Import the base converter class
from .base_converter import BaseConverter

"""
Converter class for handling CSV (Comma-Separated Values) file conversions.
Can convert CSV files to Excel (.xlsx), JSON, HTML, or keep as CSV format.
"""
class CSVConverter(BaseConverter):

    """
     Return the file formats that CSV files can be converted to.  
    """
    def get_supported_formats(self):
        # CSV can be converted to these formats
        return ['.xlsx', '.json', '.html', '.csv']

    """
    Convert a CSV file to another format (Excel, JSON, or HTML).
    """
    def convert(self, output_path):
        try:
            # Store the output path for later use
            self.output_path = output_path
            
            # Check if the input file exists before attempting to convert
            if not self.validate_input():
                print(f"Error: Input file '{self.input_path}' does not exist.")
                return False
            
            # Read the CSV file into a pandas DataFrame
            # A DataFrame is like a table with rows and columns
            print(f"Reading CSV file: {self.input_path}")
            df = pd.read_csv(self.input_path)
            
            # Extract the file extension from the output path
            # For example: 'myfile.xlsx' -> 'xlsx'
            # We use split('.') to split by dot, then [-1] to get the last part
            file_extension = output_path.split('.')[-1].lower()
            
            # Convert to the appropriate format based on the file extension
            if file_extension == 'xlsx':
                # Convert to Excel format (.xlsx)
                print(f"Converting to Excel format...")
                # index=False means don't save the row numbers as a column
                # engine='openpyxl' tells pandas to use the openpyxl library for Excel files
                df.to_excel(output_path, index=False, engine='openpyxl')
                
            elif file_extension == 'json':
                # Convert to JSON format (.json)
                print(f"Converting to JSON format...")
                # orient='records' means each row becomes a separate object
                # indent=2 makes the JSON file readable with proper indentation
                df.to_json(output_path, orient='records', indent=2)
                
            elif file_extension == 'html':
                # Convert to HTML format (.html)
                print(f"Converting to HTML format...")
                # index=False means don't include the row numbers in the table
                df.to_html(output_path, index=False)
                
            elif file_extension == 'csv':
                # Save as CSV with a new name
                print(f"Saving CSV file with new name...")
                df.to_csv(output_path, index=False)
            else:
                # If the file extension is not supported, show an error
                print(f"Error: Unsupported output format '.{file_extension}'")
                print(f"Supported formats: {', '.join(self.get_supported_formats())}")
                return False
            
            # successful conversion
            print(f"Conversion successful! File saved to: {output_path}")
            return True
            
        except Exception as e:
            # If any error occurs during conversion, catch and print the error message
            print(f"Error during CSV conversion: {str(e)}")
            return False
