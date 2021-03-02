""" This script is designed for getting product IDs
    by shortened URLs.
    E.g. when opening short link https://r.zdbb.net/u/6t80
    user is redirected to full path: https://www.amazon.com/gp/product/B003N9M6YI
    The last part of full path is the required ProductID: B003N9M6YI.
"""

# Importing "request" module from "urllib" library for working with requests/responses
from urllib import request as r
# Importing "BeautifulSoup" module from  library for working with requests/responses
from bs4 import BeautifulSoup as bs

# Setting a list of shortened URLs
listZDWrappedURLs = [
    "https://r.zdbb.net/u/6t7z",
    "https://r.zdbb.net/u/6t80",
    "https://r.zdbb.net/u/6t81",
    "https://r.zdbb.net/u/6t82",
    "https://r.zdbb.net/u/6tr",
    "https://r.zdbb.net/u/6t83",
    "https://r.zdbb.net/u/6t85",
    "https://r.zdbb.net/u/6tt"]

HEADER_Mozilla = {'User-Agent': 'Mozilla/5.0'}

for url in listZDWrappedURLs:
    remote_request = r.Request(url, headers=HEADER_Mozilla)
    HTML_response_object = r.urlopen(remote_request)
    parsed_HTML = bs(HTML_response_object,"html.parser")
    productLink = str(parsed_HTML.find("link",attrs={"rel":"canonical"}).get("href"))
    lastSlashPosition = productLink.rfind("/")
    productID = productLink[lastSlashPosition+1:]
    print(productID)