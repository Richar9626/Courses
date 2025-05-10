import aiohttp
import asyncio
import time
from bs4 import BeautifulSoup

start_time = time.time()
async def fetch(session, url):
    """
    Asynchronously fetches the HTML content of a given URL using aiohttp.
    """
    async with session.get(url) as response:
        return await response.text()
    
async def scrape_website(session, url):
    """
    Asynchronously scrapes a website and processes its HTML content.
    This function fetches the HTML content of the given URL using the provided
    HTTP session, parses it with BeautifulSoup, and extracts all paragraph
    elements from the webpage. The text content of each paragraph is then printed.
    Args:
        session (aiohttp.ClientSession): An active aiohttp session used to make the HTTP request.
        url (str): The URL of the website to scrape.
    Returns:
        None
    """
    html_content = await fetch(session, url)
    soup = BeautifulSoup(html_content, 'html.parser')
    # Example: Extract and print all paragraphs from the webpage
    paragraphs = soup.find_all('p')

    for paragraph in paragraphs:
        print(paragraph.text)

async def main():
    urls = [
        'https://example.com',
        'https://example.org',
        'https://example.net'
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [scrape_website(session, url) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")
