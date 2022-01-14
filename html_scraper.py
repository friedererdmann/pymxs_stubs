import os
from pydoc import doc
from bs4 import BeautifulSoup

path = "html_offline_help/wrapped-files"
file = "GUID-30B9D265-D265-469D-8DDD-FA6CCE369E72.htm.js"

file_path = os.path.join(path, file)

with open(file_path) as file:
    html = file.read()

start = 'var topic = "'
stop = '";'

html = html[len(start):-len(stop)]
html = html.replace('\\"', '"')
html = html.replace('\\n', '\n')

soup = BeautifulSoup(html, features="html.parser")

# print(soup.prettify())

keys = {
    "Constructor": "Constructor",
    "Properties:": "Properties",
    "Type In Properties:": "Type In Properties",
    "Interfaces:": "Interfaces"
}
documentation = {
    "Constructor": [],
    "Properties": [],
    "Type In Properties": [],
    "Interfaces": []
}
area = ""
current = []
empty = 0
result = soup.find(class_="body_content")
text = result.get_text().splitlines()
for i, line in enumerate(text):
    line_content = line.strip()
    print(i, line_content)
    if line_content in keys:
        if area:
            documentation[area].append(current)
            current = []
        area = keys[line_content]
        continue
    if not line_content:
        empty += 1
        continue
    else:
        if empty == 5:
            if area:
                documentation[area].append(current)
                current = []
        empty = 0
    if area:
        current.append(line_content)
    
import pprint
pprint.pprint(documentation)
# print(result.prettify())


