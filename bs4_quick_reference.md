# Beautiful Soup 4 Quick Reference

Full documentation is available [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

# Parse 

## Parse string

```python
from bs4 import BeautifulSoup as bs

# content in string
contents='<div class="row" id="titleSponsorStarts"></div><div class="row"></div>'

```

## Parse file

```python
from bs4 import BeautifulSoup as bs

# Parse the html content into soup object
with open('sponsorRaw.html') as fp:
    soup=bs(fp)

```

# Insert

## Insert inside tag

```python
from bs4 import BeautifulSoup as bs

# content in string
contents='<div class="row" id="titleSponsorStarts"></div><div class="row"></div>'

# make a soup parser
soup=bs(contents, "html.parser")

# append inside
soup.find("div", id="titleSponsorStarts").append("abc")
# result: '<div class="row" id="titleSponsorStarts">abc</div><div class="row"></div>'
```


## Append to the end of the string inside tag

```python
# append to the end of string

myString='<div class="row" id="titleSponsorStarts">abc</div>'

soup=bs(myString, 'html.parser')

soup.find("div", id="titleSponsorStarts").append("ABC")

# result: <div class="row" id="titleSponsorStarts">abcABC</div><div class="row"></div>
```


## Append to the beginning of string inside tag

```python
myString="<ul id=sideBanners>abc</ul>"

soup=bs(myString, "html.parser")

soup.find("ul").string.insert_before("DEF")

# result: <ul id="sideBanners">DEFabc</ul>
```

## Insert after tag

```python
myString = '<div class="row" id="titleSponsorStarts"></div><div class="row"></div>'

soup=bs(myString, "html.parser")

soup.find("div", id="titleSponsorStarts").insert_after("def")

# result: '<div class="row" id="titleSponsorStarts"></div>def<div class="row"></div>'

```

# Query & Retrieve

## Query

```python
# Method 1: generally works well with standard attributes such as `id`. Might not work with other attributes such as `class`

soup.find("tagName", attr1=value1)

# Method 2: works with any attributes. Noti

soup.find("tagName", {"attr1": "val1"})
```

Example: 

```python
# Step 1: first find the bulk code. For example: 
sponsor = soup.find("a", id=sponsorID)

# Step 2: retrieve attribute using []. For example, to retrieve the `href` attribute of anchor tag above: 
cardID = sponsor['href']
```

