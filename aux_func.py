from bs4 import BeautifulSoup as soup
from splinter import Browser

def getParsedWebpage(browser, url):
    """
    INSERT DOCSTRING HERE
    """
    browser.visit(url)
    html = browser.html
    webpage = soup(html, 'html.parser')
    
    return webpage;