# Documents scraping from UOIS

## Milestones
    20.3.2024 zahájení semestru, první den.
    26.3.2024 github repozitář.
    18.4.2024 První projektový den (demonstrace vektoru dat extrahovaných ze zdroje), popis zdroje, popis zpracování vstupu.
    14.5.2024 Druhý projektový den (kompletní data pro splnění, prezentace získávání dat).
    10.6.2024 Třetí projektový den, prezentace komplexní funkcionality včetně plnění GQL endpointu.
    12.6.2024 Poslední možnost náhrad.

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
