import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def is_valid_url(url):
    # Helper function to check if a URL is valid
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_links(url):
    # Helper function to retrieve all links from a web page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = set()

    for anchor_tag in soup.find_all("a"):
        href = anchor_tag.attrs.get("href", "")
        if is_valid_url(href):
            links.add(href)
    return links

def verify_links(url):
    # Function to verify broken links on a web page
    all_links = get_all_links(url)
    broken_links = {}

    for link in all_links:
        full_link = urljoin(url, link)
        try:
            response = requests.head(full_link)
            response.raise_for_status()
        except requests.exceptions.RequestException:
            parsed_link = urlparse(link)
            broken_links[full_link] = parsed_link.path

    return broken_links

if __name__ == "__main__":
    target_url = input("Enter the URL to verify broken links: ")
    broken_links = verify_links(target_url)

    if broken_links:
        print("Broken links found:")
        for link, path in broken_links.items():
            print(f"Link: {link} | Path: {path}")
    else:
        print("No broken links found.")
