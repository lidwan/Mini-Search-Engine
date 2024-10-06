import requests
from bs4 import BeautifulSoup


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
