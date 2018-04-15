# dic_to


## About

> Module for python dictionary converting to *xml, object etc.*


## Usage

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
>>> < xml text >
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
 <tiger name="warning">
  texttexttexttexttext
 </tiger>
</animal>

```