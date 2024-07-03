# Documents scraping from UOIS

## Milestones

    20.3.2024 zahájení semestru, první den.
    26.3.2024 github repozitář.
    18.4.2024 První projektový den (demonstrace vektoru dat extrahovaných ze zdroje), popis zdroje, popis zpracování vstupu.
    14.5.2024 Druhý projektový den (kompletní data pro splnění, prezentace získávání dat).
    10.6.2024 Třetí projektový den, prezentace komplexní funkcionality včetně plnění GQL endpointu.
    12.6.2024 Poslední možnost náhrad.

## Create new folders and file in the root folder

```bash
mkdir scraped
mkdir test_pdf
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
│   |───uois_documents
│   | 
|   │   main.py
│   |    │   ...
│   |    │   ...
|   |
│   └───dspace_documents
|
│        │   AddBitstreamsItem.py
│        │   ...
│        │   ...
│
└───scraped
│   │   file.pdf (downloaded files)
│   │   ...
|
└───test_pdf
|   │   file.pdf (fake pdf for upload)
|   │   ...
│
│
└───secret
    │   passwords.json
    |   url.json


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
  "downloads_folder": "C:\\Users\\user\\Documents\\..."
}
```

## Edit url.json

```json
[
  {
    "url": "https://intranet.unob.cz/dokum/predpisymsmt/Forms/AllItems.aspx"
  },
  {
    "url": "https://intranet.unob.cz/dokum/predpisyrektor/Forms/AllItems.aspx"
  },
  {
    "url": "https://intranet.unob.cz/dokum/OpatreniDekanu/Forms/AllItems.aspx"
  }
]
```
