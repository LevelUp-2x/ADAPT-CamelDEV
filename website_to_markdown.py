import os
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import html2text
import concurrent.futures

def download_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return None

def html_to_markdown(html_content):
    h = html2text.HTML2Text()
    h.ignore_links = False
    return h.handle(html_content)

def save_markdown(content, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def get_links(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')
    return [urljoin(base_url, link.get('href')) for link in soup.find_all('a', href=True)]

def is_valid_url(url, base_domain):
    parsed_url = urlparse(url)
    return parsed_url.netloc == base_domain and parsed_url.scheme in ('http', 'https')

def process_page(url, base_url, base_domain, output_dir):
    if not is_valid_url(url, base_domain):
        return

    html_content = download_page(url)
    if html_content is None:
        return

    markdown_content = html_to_markdown(html_content)
    
    relative_path = urlparse(url).path
    if relative_path.endswith('/'):
        relative_path += 'index'
    elif not relative_path.endswith('.html'):
        relative_path += '.html'
    
    output_path = os.path.join(output_dir, relative_path.lstrip('/').replace('.html', '.md'))
    save_markdown(markdown_content, output_path)
    print(f"Saved: {output_path}")

    return get_links(html_content, base_url)

def download_site(start_url, output_dir):
    base_url = start_url
    base_domain = urlparse(start_url).netloc
    
    urls_to_process = [start_url]
    processed_urls = set()

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        while urls_to_process:
            futures = []
            for url in urls_to_process[:5]:  # Process 5 URLs at a time
                if url not in processed_urls:
                    processed_urls.add(url)
                    futures.append(executor.submit(process_page, url, base_url, base_domain, output_dir))
            
            urls_to_process = urls_to_process[5:]
            
            for future in concurrent.futures.as_completed(futures):
                new_links = future.result()
                if new_links:
                    urls_to_process.extend([link for link in new_links if link not in processed_urls])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python website_to_markdown.py <start_url> <output_dir>")
        sys.exit(1)
    
    start_url = sys.argv[1]
    output_dir = sys.argv[2]
    
    download_site(start_url, output_dir)
    print("Conversion completed!")