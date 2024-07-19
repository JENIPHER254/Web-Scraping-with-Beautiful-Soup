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

# =============================== SEARCHING IN A TREE WITH FILTERS ==========================
htmlPage = "test.html"
with open(htmlPage,"r")as organization: soup2=BeautifulSoup(organization,"lxml")
soup2.contents