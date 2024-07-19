# Web-Scraping-with-Beautiful-Soup
Web Scraping Basics. Using Html.parser, beautiful soup and python to achieve web craping.


## Find and Find_all methods

### Find_all() method
- scans entire document if match found returns list with values else returns empty list
- Associated functions include: find_parents(), find_previous_siblings(), find_all_next(), find_all_previous(),
find_next_siblings() = All these scan for all matches in the document/tree

### Find() method
- Searches only for passed arguments and returns only the first matched value else returns none
- Associated functions include: find_parent(), find_previous_sibling(), find_next(), find_previous(),
find_next_sibling() = All these scan only for the first  match in the document/tree

### lxml parser installation
- pip install lxml