import os
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urldefrag
import html2text
import concurrent.futures
import re
import logging
from datetime import datetime

# Set up logging
log_file = f"website_to_markdown_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_info(message):
    print(message)
    logging.info(message)

def log_error(message):
    print(f"ERROR: {message}", file=sys.stderr)
    logging.error(message)

def download_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        log_error(f"Error downloading {url}: {e}")
        return None

def html_to_markdown(html_content):
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.body_width = 0  # Disable line wrapping
    return h.handle(html_content)

def save_markdown(content, filepath):
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        log_info(f"Saved: {filepath}")
    except IOError as e:
        log_error(f"Error saving file {filepath}: {e}")

def get_links(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')
    return [urljoin(base_url, link.get('href')) for link in soup.find_all('a', href=True)]

def is_valid_url(url):
    parsed_url = urlparse(url)
    return parsed_url.scheme in ('http', 'https')

def url_to_filepath(url, output_dir):
    parsed_url = urlparse(url)
    path = parsed_url.path
    if path.endswith('/'):
        path += 'index'
    elif not path.endswith('.html'):
        path += '.html'
    return os.path.join(output_dir, path.lstrip('/').replace('.html', '.md'))

def update_links(content, url, output_dir):
    def replace_link(match):
        link = match.group(1)
        full_url = urljoin(url, link)
        filepath = url_to_filepath(full_url, output_dir)
        if os.path.exists(filepath):
            return f'({os.path.relpath(filepath, os.path.dirname(url_to_filepath(url, output_dir)))})'
        return match.group(0)

    return re.sub(r'\(((?:http|https)://[^\)]+)\)', replace_link, content)

def process_page(url, output_dir, processed_urls):
    if not is_valid_url(url) or url in processed_urls:
        return []

    processed_urls.add(url)
    log_info(f"Processing: {url}")

    html_content = download_page(url)
    if html_content is None:
        return []

    try:
        markdown_content = html_to_markdown(html_content)
        markdown_content = update_links(markdown_content, url, output_dir)
        
        output_path = url_to_filepath(url, output_dir)
        save_markdown(markdown_content, output_path)

        return get_links(html_content, url)
    except Exception as e:
        log_error(f"Error processing {url}: {e}")
        return []

def download_site(start_url, output_dir):
    urls_to_process = [start_url]
    processed_urls = set()
    failed_urls = set()

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        while urls_to_process:
            futures = []
            for url in urls_to_process[:5]:  # Process 5 URLs at a time
                if url not in processed_urls:
                    futures.append(executor.submit(process_page, url, output_dir, processed_urls))
            
            urls_to_process = urls_to_process[5:]
            
            for future in concurrent.futures.as_completed(futures):
                try:
                    new_links = future.result()
                    if new_links:
                        urls_to_process.extend([link for link in new_links if link not in processed_urls])
                except Exception as e:
                    log_error(f"Error in future: {e}")
                    failed_urls.add(url)

    log_info(f"Processed URLs: {len(processed_urls)}")
    log_info(f"Failed URLs: {len(failed_urls)}")
    if failed_urls:
        log_info("Failed URLs:")
        for url in failed_urls:
            log_info(url)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python website_to_markdown.py <start_url> <output_dir>")
        sys.exit(1)
    
    start_url = sys.argv[1]
    output_dir = sys.argv[2]
    
    log_info(f"Starting conversion from {start_url} to {output_dir}")
    download_site(start_url, output_dir)
    log_info("Conversion completed!")
    log_info(f"Log file: {log_file}")