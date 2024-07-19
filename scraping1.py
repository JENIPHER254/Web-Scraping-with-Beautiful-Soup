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

print(" =============================== SEARCHING IN A TREE WITH FILTERS ==========================")
htmlPage = "test.html"
with open(htmlPage,"r")as organization: soup2=BeautifulSoup(organization,"lxml")
soup2.contents
print(soup2.find("li")) 
print(soup2.find_all(text=["section", "page","About"]))
# finding using associated css
print(soup2.find(attrs={"class":"home"}))
# Searching document based on id
print(" =============================== SEARCHING SPECIFIC ID ==========================")
def  test_function(tag):
    return tag.has_attr("id") and tag.get("id")=="about"

contact =soup2.find(test_function)
print(contact)
print(" =============================== PRINTING ALL THE TAG NAMES IN THE DOCUMENTS ==========================")
def allTagNames():
    for tag in soup.findAll(True):
        print(tag.name)

allTagNames()
print(" =============================== PARENT AND SIBLING FUNCTIONS ==========================")
mainChar = soup2.find(id="about")
findSibling = mainChar.find_next_sibling()
findSibling2 = mainChar.find_previous_sibling()
findParent = mainChar.find_parent()

print(findParent)
