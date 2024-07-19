from bs4 import  BeautifulSoup
import re

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
myEmail = re.compile("\w+@\w+\.\w+")
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