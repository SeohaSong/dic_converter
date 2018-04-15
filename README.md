# aws_handler


## About

> Module for python dictionary converting to *xml, object etc.*


## Usage

```python

from dic_to import arrdic2xml


arrdic = [
    {"div name='myname' type='mytype'": [
        {"a": "text"},
        {"a": "texttext"},
        {"span name='myspan'": "texttexttexttexttext"}
    ]}
]

bs = arrdic2xml.convert(arrdic)
print(bs.prettify())

>>> <?xml version="1.0" encoding="utf-8"?>
... <div name="myname" type="mytype">
...  <a>
...   text
...  </a>
...  <a>
...   texttext
...  </a>
...  <span name="myspan">
...   texttexttexttexttext
...  </span>
... </div>

```