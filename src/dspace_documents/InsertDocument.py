import aiohttp
import json
from config import DSPACE_DOMAIN, DSPACE_PORT, COLLECTION_ID

async def insertDocument(name,description="sraped dokument",author_id = "89d1e724-ae0f-11ed-9bd8-0242ac110002",collection_id = COLLECTION_ID,type="pdf",language="cz"):

    async with aiohttp.ClientSession() as session:
        url = f"{DSPACE_DOMAIN}:{DSPACE_PORT}/gql/"
    
        headers = {
            "Content-Type": "application/json",
        }

        data = json.dumps(
            {"query": f'mutation insert{{documentInsert(document:{{name:"{name}",description:"{description}",authorId:"{author_id}"}},collectionId:"{collection_id}",type:"{type}",language:"{language}" ){{id}}}}',"operationName": "insert"}
        )
        
        async with session.post(
            url, headers=headers, data=data
        ) as response:
              
            result = await response.json()
            id = result["data"]["documentInsert"]["id"]

            return id
