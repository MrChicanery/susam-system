import os
import re

# === CONFIG ===
input_path = r"courses.txt"         # Path to the input file
output_dir = r"./courses"       # Output directory for generated .mdx files

# Optional: Map course prefixes to full department names
department_names = {
    "AGR": "Agriculture",
    "BUA": "Accounting",
    "BUE": "Entrepreneurship",
    "BUG": "General Business",
    "BUH": "Health Business",
    "BUN": "Engineering Business",
    "BUR": "Rail Business",
    "ECO": "Economics",
    "ECS": "Social Ecology and Environmental Justice",
    "EDB": "Building Design",
    "EDR": "Rail Design",
    "ENC": "English Writing",
    "GSW": "Gender, Sexuality, and Women’s Studies",
    "HIS": "History",
    "IDS": "Interdisciplinary Studies",
    "ILS": "Interlearning Studies",
    "LSF": "Foundation of Law",
    "LSC": "Civil Law",
    "LSR": "Criminal Law",
    "LSB": "Business Law",
    "LSI": "International Law",
    "MAC": "Pure Math Courses",
    "MAS": "Statistical Math",
    "MIG": "General Military",
    "MIO": "Military Operations",
    "PHI": "Philosophy",
    "POL": "Politics and International Affairs",
    "SLF": "Slimefun"
    # Add more as needed
}


# Parse the input file
with open(input_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

courses_by_prefix = {}
current_prefix = None

# Pattern to match lines like: POL (Politics and International Affairs)
dept_line_pattern = re.compile(r"^([A-Z]{2,4})\s+\((.+?)\)\s*$")

for line in lines:
    line = line.strip()
    if not line:
        continue

    # Capture department name
    match = dept_line_pattern.match(line)
    if match:
        prefix, dept_name = match.groups()
        department_names[prefix] = dept_name
        current_prefix = prefix
        courses_by_prefix[current_prefix] = []
        continue

    # Capture course codes (like POL-1000) and titles
    if current_prefix and re.match(rf"^{current_prefix}-\d+", line):
        code, title = line.split(" ", 1)
        courses_by_prefix[current_prefix].append((code, title.strip()))

# Create output directory if needed
os.makedirs(output_dir, exist_ok=True)

# Write out .mdx files
for prefix, course_list in courses_by_prefix.items():
    dept_title = department_names.get(prefix, prefix)
    filename = f"{prefix}.mdx"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"""---
title: "{dept_title} Courses ({prefix})"
slug: "{prefix}"
description: ""
---

""")
        for code, title in course_list:
            f.write(f"- **{code}**: {title}\n")

print(f"✅ Finished generating {len(courses_by_prefix)} department files in: {output_dir}")
