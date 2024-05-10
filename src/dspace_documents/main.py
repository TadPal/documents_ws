import aiohttp
import asyncio
import json
import os
from AddBitstreamsItem import addBitstreamsItem
from AddBundleItem import addBundleItem
from CreateWorkspaceItem import createWorkspaceItem
from AddTittleItem import addTitleItem
from CreateItem import createItem
from config import DSPACE_DOMAIN, DSPACE_PORT, BASE_FOLDER, COLLECTION_ID


async def process_pdf_files(base_folder=BASE_FOLDER):

    # establishing session in 3 steps
    async with aiohttp.ClientSession() as session:

        # step 1: Get XSRF token from cookie
        url_step1 = f"{DSPACE_DOMAIN}:{DSPACE_PORT}/server/api/authn/status"
        headers_step1 = {"Content-Type": "application/x-www-form-urlencoded"}

        async with session.get(url_step1, headers=headers_step1) as response_step1:
            xsrf_cookie = response_step1.cookies.get("DSPACE-XSRF-COOKIE").value

            url_step2 = f"{DSPACE_DOMAIN}:{DSPACE_PORT}/server/api/authn/login"
            headers_step2 = {
                "Content-Type": "application/x-www-form-urlencoded",
                "X-XSRF-TOKEN": xsrf_cookie,
            }
            params_step2 = {"user": "test@test.edu", "password": "admin"}
        
        # step 2: Login and obtain Bearer token
        async with session.post(
            url_step2, headers=headers_step2, data=params_step2
        ) as response_step2:
            bearer_token = response_step2.headers.get("Authorization")
            xsrf_cookie = response_step2.cookies.get("DSPACE-XSRF-COOKIE").value

        url_step3 = (
            f"{DSPACE_DOMAIN}:{DSPACE_PORT}/server/api/submission/workspaceitems"
        )
        headers_step3 = {}
        data_step3 = {}

        # step 3: Access a new API endpoint
        async with session.post(
            url_step3, headers=headers_step3, data=json.dumps(data_step3)
        ) as response_step3:
            # Print the response for Step 3
            xsrf_cookie_step3 = response_step3.cookies.get(
                "DSPACE-XSRF-COOKIE").value


        """Processes PDF files in the given directory by printing their names."""
        for entry in os.listdir(BASE_FOLDER):
            if entry.endswith('.pdf') and os.path.isfile(os.path.join(BASE_FOLDER, entry)):
                # Here, 'entry' is the name of a PDF file
                document_name = entry

                # Vytvoření itemu
                #item_result = await createWorkspaceItem(bearer_token, xsrf_cookie_step3, session)
                item_result = await createItem(bearer_token, xsrf_cookie_step3, session, collectionId=COLLECTION_ID, title=document_name)
                itemId = item_result['response']['uuid']


                # Add title of item
                await addTitleItem(bearer_token, xsrf_cookie_step3, session, itemId, titleName = document_name, language="cz" )
                
                # Přidání bundle k itemu
                bundle_result = await addBundleItem(bearer_token, xsrf_cookie_step3, session, itemId)
                bundleId = bundle_result['response']['uuid']

                # Nahrání PDF souboru
                bitstream_result = await addBitstreamsItem(bearer_token, xsrf_cookie_step3, session, base_folder, bundleId, document_name)
        
                print(f"Created DSpace item with uuid, {itemId}, and pdf uploaded\n")



asyncio.run(process_pdf_files())
