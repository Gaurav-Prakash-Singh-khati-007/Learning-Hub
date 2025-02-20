import os
import json
import zipfile
# import rarfile
import shutil
import re
from natsort import natsorted

def extract_archive(file_path, extract_to):
    """Extracts ZIP or RAR files and deletes them after extraction."""
    try:
        if file_path.endswith(".zip"):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
        elif file_path.endswith(".rar"):
            with rarfile.RarFile(file_path, 'r') as rar_ref:
                rar_ref.extractall(extract_to)
        os.remove(file_path)  # Delete the archive after extraction
    except Exception as e:
        print(f"Error extracting {file_path}: {e}")

def generate_sections(folder_path, output_file):
    sections = []

    for subfolder in natsorted(os.listdir(folder_path)):  # Natural sorting
        subfolder_path = os.path.join(folder_path, subfolder)

        if os.path.isdir(subfolder_path):
            # Extract archives first
            for file in os.listdir(subfolder_path):
                file_path = os.path.join(subfolder_path, file)
                if file.endswith((".zip", ".rar")):
                    extract_archive(file_path, subfolder_path)

            # Process files after extraction
            files = [
                {"name": os.path.splitext(file)[0], "path": os.path.join(subfolder, file).replace("\\", "/")}
                for file in natsorted(os.listdir(subfolder_path))  # Natural sorting
                if os.path.isfile(os.path.join(subfolder_path, file)) and not file.endswith((".srt", ".url"))
            ]

            if files:  # Add section only if it contains valid files
                sections.append({"name": subfolder, "files": files})

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("const sections = " + json.dumps(sections, indent=2) + ";")

# Example usage
folder_path = os.path.expanduser("~/Downloads/Study/TechStudy/UPSC BOOKS")
# folder_path = os.path.expanduser("~/Downloads/Study/TechStudy/ccna")
output_file = "sections.txt"
generate_sections(folder_path, output_file)
