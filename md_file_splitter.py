import os\r
import re\r
\r
def split_md_file(input_file, output_dir, lines_per_file=2000):\r
    # Create output directory if it doesn't exist\r
    os.makedirs(output_dir, exist_ok=True)\r
\r
    # Read the input file\r
    with open(input_file, 'r', encoding='utf-8') as f:\r
        content = f.readlines()\r
    print(f'Content Length: {len(content)}')\r
\r
    # Calculate the number of output files needed\r
    num_files = -(-len(content) // lines_per_file)  # Ceiling division\r
    print(f'Number of Files: {num_files}')\r
\r
    # Split the content into separate files\r
    for i in range(num_files):\r
        print(f'Iteration: {i}')\r
        start_line = i * lines_per_file\r
        print(f'Start Line: {start_line}')\r
        end_line = (i + 1) * lines_per_file\r
        print(f'End Line: {end_line}')\r
        output_file = os.path.join(output_dir, f'{os.path.splitext(input_file)[0]}_part_{i+1}.md')\r
        with open(output_file, 'w', encoding='utf-8') as f:\r
            f.writelines(content[start_line:end_line])\r
\r
    print(f"Split {num_files} files created in {output_dir}")\r
\r
# # Usage\r
# input_file = r"C:\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Users\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ChaseRemmen\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ADAPT\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ADAPT-CamelDEV\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Resume\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\CAMMY\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\CAMMY16.md"\r
# output_dir = r"C:\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Users\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ChaseRemmen\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ADAPT\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ADAPT-CamelDEV\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Resume\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\CAMMY\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\CAMMY16_split"\r
# split_md_file(input_file, output_dir)