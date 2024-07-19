import requests
from bs4 import  BeautifulSoup ,SoupStrainer #used for parsing part of a document
import re
from urllib.request import urlopen #used to read url and parse the contents

html_doc= """
<html>

    <head><title>Web Scraping></title></head>
    <body>
        <b><!-- This line is a comment--></b>
        <h1>SCRAPING</h1>
        <employee>testing this theory</employee>
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
print(" =============================== USING REGULAR EXPRESSION  ==========================")
emailExample = "<br><h1>Searching tor the email</h1><p>jeniperkuki@gmail.com</p><p>onyangoje123@gmail.com</p>"
soup3 = BeautifulSoup(emailExample,"lxml")
myEmail = re.compile(r"\w+@\w+\.\w+")
email_id = soup3.findAll(text=myEmail)
print (email_id[1])
print(" =============================== MODIFYING A TREE  ==========================")
tag = soup.employee
# adding a class to the employee tag
tag['class']= ['manager']
print(tag)
# adding a new tag
tag1= soup.new_tag('test')
tag1.string = "This is a New Test Tag"
soup.employee.insert_after(tag1)
if "This" in tag1.string:
    tag1.string = tag1.string.replace("This", "These")
print(soup)
print(" =============================== PARSING PART OF A DOCUMENT USING SOUP STRAINER ==========================")

# You can print using various methodr
# 1. prettify() method
# 2. unify(), unicode()method

tagsWithLab = SoupStrainer(id='lab')
print(BeautifulSoup(str(soup2),'html.parser', parse_only=tagsWithLab).prettify())
# or
with open(htmlPage, "r") as organization:
    html_content = organization.read()

tagsWithLab = SoupStrainer(id='lab')
print(BeautifulSoup(html_content, 'html.parser', parse_only=tagsWithLab).prettify())

print(" =============================== PRINTING AND FORMATTING ==========================")
url='https://simplilearn.com'
result = requests.get(url)
pageContent = result.content
soup4 = BeautifulSoup(pageContent,'html.parser')
# view the file in html read form
print(soup4.prettify())
print(" =============================== ENCODING DOCUMENT ==========================")
# view the encoding of the document
print(soup4.original_encoding)
print(soup4.head)
# finding all link information
for href in soup4.findAll('a',href=True):
    print(href['href'])

# Method 2
url2='https://simplilearn.com/resources'
webpage = urlopen(url)
soup5 = BeautifulSoup(webpage,'html.parser')
webpage.close
print(soup5.prettify())
# finding links
for href in soup5.findAll('a', href=True):
    print(href['href'])