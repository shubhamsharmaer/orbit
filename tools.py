from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
from rich import print
import os
from dotenv import load_dotenv
load_dotenv()
# import warnings

# warnings.filterwarnings("ignore", category="XMLParsedAsHTMLWarning")

tavily = TavilyClient(api_key=os.getenv("TAVILY_API"))

@tool
def web_search(query: str) -> str:
    """
    Perform a web search gather reliable and most recent information on a topic and return the Titles, URLs, and snippets.
    """

    tavily_results = tavily.search(query, max_results=5)
    
    out = []
    for r in tavily_results['results']:
        out.append(f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n")

    return "\n-----\n".join(out)

# print(web_search.invoke({"query": "What is new about tesla roadster?"}))

@tool
def web_scraper(url: str) -> str:
    """
    Scrape the content of a webpage and return the text.
    """
    try:
        response = requests.get(url, timeout=6, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        for tag in soup(['script', 'style', 'footer', 'nav']):
            tag.decompose()
        text = soup.get_text(separator=' ', strip=True)[:3000]
        return text
    except requests.exceptions.RequestException as e:
        return f"Error fetching the URL: {e}"

# print(web_scraper.invoke({"url": "https://timesofindia.indiatimes.com/technology/tech-news/years-after-telling-meta-employees-to-inflict-pain-on-apple-mark-zuckerberg-sends-thanks-note-to-apple-ceo-john-ternus-gets-a-reply/articleshow/134985222.cms"}))