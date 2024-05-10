import json
from config import DSPACE_DOMAIN, DSPACE_PORT


async def addBundleItem(bearer_token,xsrf_cookie_step3, session, itemsId):

        # Step 4: Another API endpoint using XSRF cookie from Step 3
        url_step4 = f"{DSPACE_DOMAIN}:{DSPACE_PORT}/server/api/core/items/{itemsId}/bundles"

        headers_step4 = {
            "Content-Type": "application/json",
            "Authorization": bearer_token,
            "X-XSRF-TOKEN": xsrf_cookie_step3,  # Use XSRF cookie from Step 3
        }
        data_step4 = {
                "name": "ORIGINAL",
                "metadata": {}
            }
        
        async with session.post(
            url_step4, headers=headers_step4, data=json.dumps(data_step4)
        ) as response_step4:
            # Print the response for Step 4
            result = {}
        
            result["response"] = await response_step4.json()
            result["msg"] = response_step4.status
            
            return result
