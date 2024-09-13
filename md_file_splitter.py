import os
import re

def split_md_file(input_file, output_dir, lines_per_file=2000):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split the content at "**User:**" occurrences
    splits = re.split(r'(?=\*\*User:\*\*)', content)

    # Combine splits into chunks of approximately 2000 lines
    chunks = []
    current_chunk = []
    current_lines = 0

    for split in splits:
        split_lines = split.count('\n')
        if current_lines + split_lines > lines_per_file and current_chunk:
            chunks.append('\n'.join(current_chunk))
            current_chunk = []
            current_lines = 0
        current_chunk.append(split)
        current_lines += split_lines

    if current_chunk:
        chunks.append('\n'.join(current_chunk))

    # Write chunks to separate files
    for i, chunk in enumerate(chunks):
        output_file = os.path.join(output_dir, f'CAMMY16_part{i+1}.md')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(chunk)

    print(f"Split {len(chunks)} files created in {output_dir}")

# Usage
input_file = r"C:\Users\ChaseRemmen\ADAPT\ADAPT-CamelDEV\Resume\CAMMY\CAMMY16.md"
output_dir = r"C:\Users\ChaseRemmen\ADAPT\ADAPT-CamelDEV\Resume\CAMMY\CAMMY16_split"
split_md_file(input_file, output_dir)