from bs4 import  BeautifulSoup

html_doc= """
<html>

    <head><title>Web Scraping></title></head>
    <body>
        <b><!-- This line is a comment--></b>
        <h1>WEB SCRAPING</h1>
    </body>
   
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print(type(soup))
print(soup)
print(soup.h1)
print(soup.b.string)
