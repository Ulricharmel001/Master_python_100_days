# wikipedia article scraper
import requests
from bs4 import BeautifulSoup

# step1: get wikipedia article url
def get_wikipedia_article_url(article_name):
    base_url = f"https://en.wikipedia.org/wiki/{article_name.replace(' ', '_')}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    response = requests.get(base_url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the article. Status code: {response.status_code}")
        return None
    
#step2: extract the article title and content
def extract_article_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    title_elem = soup.find('h1', {'id': 'firstHeading'})
    content_elem = soup.find('div', {'class': 'mw-parser-output'})
    title = title_elem.text if title_elem else "No title found"
    content = content_elem.text if content_elem else "No content found"
    return title, content

# step3: extract article summary and references
def extract_summary_and_references(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    output = soup.find('div', {'class': 'mw-parser-output'})
    summary = output.find('p').text if output and output.find('p') else "No summary found"
    references = [ref.text for ref in soup.find_all('li', {'id': lambda x: x and x.startswith('cite_note')})]
    if not references:
        references = ["No references found."]
    return summary, references

# step4: get article headings and subheadings
def get_article_headings(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    headings = [heading.text for heading in soup.find_all(['h2', 'h3', 'h4'])]
    return headings

#step5: get article images and captions
def get_article_images_and_captions(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    images = []
    for img in soup.find_all('img'):
        img_url = img.get('src')
        caption = img.get('alt', 'No caption available.')
        images.append((img_url, caption))
    return images

#step6: get article related links 
def get_article_related_links(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = [link.get('href') for link in soup.find_all('a', {'class': 'mw-redirect'})]
    return list(set(links))  

#Step7: main function to scrape the article
def scrape_wikipedia_article(article_name):
    topic = article_name.strip()
    html_content = get_wikipedia_article_url(topic)
    if html_content:
        title, content = extract_article_content(html_content)
        summary, references = extract_summary_and_references(html_content)
        headings = get_article_headings(html_content)
        images = get_article_images_and_captions(html_content)
        related_links = get_article_related_links(html_content)

        print(f"Title: {title}\n")
        print(f"Summary: {summary}\n")
        print(f"Headings: {headings}\n")
        print(f"Images and Captions: {images}\n")
        print(f"References: {references}\n")
        print(f"Related Links: {related_links}\n")

# run the scraper
if __name__ == "__main__":
    topic = input("Enter the Wikipedia article name: ").strip()
    scrape_wikipedia_article(topic)