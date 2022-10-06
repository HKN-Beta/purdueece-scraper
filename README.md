# purdueece-scraper

Scrapes purdueece.com articles into a JSON file via a CGI script on Apache, which 
is then rendered in a TV-friendly format.

Libraries used:
- requests (Python, fetches HTML)
- BeautifulSoup (Python, parses HTML)
- qrcode.js (Client-side JS, Renders QR code for each article's URL)
- PDF.js (Client-side JS, Renders any PDFs in article)

