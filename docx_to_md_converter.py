import os
import docx2txt

def convert_docx_to_md(docx_path, md_path):
    # Extract text from DOCX
    text = docx2txt.process(docx_path)
    
    # Write text to MD file
    with open(md_path, 'w', encoding='utf-8') as md_file:
        md_file.write(text)

def main():
    directory = r"C:\Users\ChaseRemmen\ADAPT\ADAPT-CamelDEV\Planning"
    
    for filename in os.listdir(directory):
        if filename.endswith(".docx"):
            docx_path = os.path.join(directory, filename)
            md_filename = os.path.splitext(filename)[0] + ".md"
            md_path = os.path.join(directory, md_filename)
            
            print(f"Converting {filename} to {md_filename}")
            convert_docx_to_md(docx_path, md_path)
    
    print("Conversion complete!")

if __name__ == "__main__":
    main()