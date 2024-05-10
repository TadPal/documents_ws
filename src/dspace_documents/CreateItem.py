import json
from config import DSPACE_DOMAIN, DSPACE_PORT


async def createItem(bearer_token,xsrf_cookie_step3, session, collectionId, title, author="",type="",language="cz"):

            # Step 4: Another API endpoint using XSRF cookie from Step 3
            url_step4 = (
                f"{DSPACE_DOMAIN}:{DSPACE_PORT}/server/api/core/items?owningCollection={collectionId}"
            )
            headers_step4 = {
                "Content-Type": "application/json",
                "Authorization": bearer_token,
                "X-XSRF-TOKEN": xsrf_cookie_step3,  # Use XSRF cookie from Step 3
            }
            
            data_step4 = {
              "name": f"{title}",
              "metadata": {
                "dc.contributor.author": [
                  {
                    "value": f"{author}",
                    "language": f"{language}",
                    "authority": "null",
                    "confidence": -1
                  }
                ],
                "dc.title": [
                  {
                    "value": f"{title}",
                    "language": f"{language}",
                    "authority": "null",
                    "confidence": -1
                  }
                ],
                "dc.type": [
                  {
                    "value": f"{type}",
                    "language": f"{language}",
                    "authority": "null",
                    "confidence": -1
                  }
                ]
              },
              "inArchive": "true",
              "discoverable": "true",
              "withdrawn": "false",
              "type": "item"
            }

            async with session.post(
                url_step4, headers=headers_step4, data=json.dumps(data_step4)
            ) as response_step4:
                
                result = {}

                result["msg"] = response_step4.status
                result["response"] = await response_step4.json()
                return result



