import json
from config import DSPACE_DOMAIN, DSPACE_PORT


async def addTitleItem(bearer_token, xsrf_cookie_step3, session, itemsId, titleName, language="cz"):

            # Step 4: Another API endpoint using XSRF cookie from Step 3
            url_step4 = f"{DSPACE_DOMAIN}:{DSPACE_PORT}/server/api/core/items/{itemsId}"
            headers_step4 = {
                "Content-Type": "application/json",
                "Authorization": bearer_token,
                "X-XSRF-TOKEN": xsrf_cookie_step3,  # Use XSRF cookie from Step 3
            }
            data_step4 = [
                {
                    "op": "add",
                    "path": "/metadata/dc.title/0",
                    "value": {"value": f"{titleName}", "language": f"{language}"},
                }
            ]

            async with session.patch(
                url_step4, headers=headers_step4, data=json.dumps(data_step4)
            ) as response_step4:
                # Print the response for Step 4
                result = {}
        
                result["msg"] = response_step4.status
                result["response"] = await response_step4.json()
                        
                return result



