from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import re
html = """
<root>
<item><name>A</><value>0</></>
<item><name>B</><value>3</></>
<item><name>C</><value>1</></>
</root>"""
soup = BeautifulSoup(html,"xml").prettify()
root = ET.fromstring(soup)
for item in root.findall('item'):
  name = item.find('name').text
  value = int(item.find('value').text)
  if value > 1 or value == 1:
    print(re.sub("^\s+|\n|\r|\s+$", '', name))
