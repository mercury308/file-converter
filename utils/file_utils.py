import os
from pathlib import Path
from datetime import datetime

def validate_file(file_path, supported_formats):
    """Validate if the file exists and is of a supported format."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    if not any(file_path.endswith(ext) for ext in supported_formats):
        raise ValueError(f"The file format of {file_path} is not supported.")
    
    return True

def get_output_path(input_path, target_format):
    """Generate an output file path based on the input file and target format."""
    base, _ = os.path.splitext(input_path)
    return f"{base}_converted.{target_format}"

def get_file_extension(file_path):
    """Get the file extension from a file path."""
    return Path(file_path).suffix.lower()

def ensure_directory_exists(file_path):
    """Ensure that the directory for the given file path exists."""
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)