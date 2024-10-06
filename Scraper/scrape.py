import requests
from bs4 import BeautifulSoup
import json
import time

# fetches news articles from the roya news website when given a specific article number.
def fetch_article(article_id):
    url = f"https://en.royanews.tv/news/{article_id}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return None  # Skip article if the page is not found

    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title and content based on updated tag structure
    try:
        title = soup.find('h1').get_text() # Roya always uses h1's for article titles (based on a quick look around their websites html)
        content_paragraphs = soup.find_all('p') # same goes for article details, always p tags!
        content = ' '.join(paragraph.get_text() for paragraph in content_paragraphs)
    except AttributeError:
        return None  # Skip if the structure isn't as expected

    return {
        'id': article_id,
        'title': title,
        'content': content,
        'link': url
    }

# when start = 40000 & end = 54762 that's one whole year of news articles.
def scrape_articles(start_id=40000, end_id=54762, output_file="articles.json"):
    articles = []
    for article_id in range(start_id, end_id + 1):
        article = fetch_article(article_id)
        if article:
            articles.append(article)
            print(f"Fetched article {article_id}")
        time.sleep(0.5)  # don't overwhelm the server ;) stuck in my head thanks IR course!
    # Save the articles to a JSON file
    with open(output_file, 'w') as f:
        json.dump(articles, f)

    print("Scraping complete.")

# Run the scraper
scrape_articles()
