import json
import re

# Read the text file
with open("../ccna/sections.txt", "r", encoding="utf-8") as file:
    content = file.read().strip()  # Remove leading/trailing spaces

# Remove "const sections =" if present
content = re.sub(r"^const sections\s*=\s*", "", content, flags=re.MULTILINE)

# Fix trailing commas in JSON arrays/objects
content = re.sub(r",\s*([\]}])", r"\1", content)

# Attempt to parse JSON
try:
    sections = json.loads(content)  # Convert to Python dictionary
    with open("sections.json", "w", encoding="utf-8") as json_file:
        json.dump(sections, json_file, indent=4, ensure_ascii=False)
    print("✅ JSON file 'sections.json' created successfully!")
except json.JSONDecodeError as e:
    print("❌ Error: Invalid JSON format! Check for syntax issues.")
    print(e)
