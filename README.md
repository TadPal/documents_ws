# Documents scraping from UOIS

## Create 2 new folders in the root folder

```bash
mkdir scraped

mkdir secret
touch passwords.json
```

## Your folder should look like this

```
DOCUMENTS_WS
│   README.md
│   requirements.txt
│   .gitignore
│
└───src
│   │
│   │
│   │
│   └───uois_documents
│       │   json_object_scraper.py
│       │   ...
│       │   ...
│
└───scraped
│   │   object_1.json (this file is created automatically)
│   │   ...
│
│
└───secret
    │   passwords.json


```

## Edit passwords.json

**The username and pasword must be base64 encoded** <br />
|<br />
|<br />
v<br />
_[CyberChef](<https://gchq.github.io/CyberChef/#recipe=To_Base64('A-Za-z0-9%2B/%3D')&input=cGFzc3dvcmQ>) online encoding tool_

```json
{
  "user": {
    "name": "xxx",
    "pass": "xxx"
  }
}
```
