# dic_converter


## About

> Module for converting python-dictionary to *xml, object etc.*


## Usage

### Dictionary => Object

```python

from dic_to import dic2obj


dic = {"a": 1, "b": {"c": 2}}
obj = dic2obj.convert(dic)

print(obj.a)

>>> 1

print(obj.b.c)

>>> 2

```

### Array-Dictionary => XML

```python

from dic_to import arrdic2xml


arrdic = [
    {"animal name='myname' type='mytype'": [
        {"cat": "text"},
        {"horse": "texttext"},
        {"tiger type='warning'": "texttexttexttexttext"}
    ]}
]

bs = arrdic2xml.convert(arrdic)
print(bs.prettify())

>>> ...(below xml text)

```

```xml

<?xml version="1.0" encoding="utf-8"?>
<animal name="myname" type="mytype">
 <cat>
  text
 </cat>
 <horse>
  texttext
 </horse>
 <tiger type="warning">
  texttexttexttexttext
 </tiger>
</animal>

```