import aiohttp
import asyncio
import json

from config import DSPACE_DOMAIN, DSPACE_PORT

async def insertContent(id, filename, file_path):
    lastchange = "2024-05-13 18:03:00.839086"

    url = f"{DSPACE_DOMAIN}:{DSPACE_PORT}/gql/"
    headers = {
        "Content-Type": "application/json",
    }
    
    data = json.dumps( 
        {"query": f'mutation{{dspaceAddBitstream(document: {{id: "{id}", lastchange: "{lastchange}"}},filename: "{filename}",filePath: "{file_path}") {{msg response}}}}'}
    ) 
    print("data:",data)

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=data) as response:
            result = await response.json()
            print(result)

            return result