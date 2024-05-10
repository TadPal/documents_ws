import aiohttp
import json
import os
from config import DSPACE_DOMAIN, DSPACE_PORT

async def addBitstreamsItem(bearer_token, xsrf_cookie_step3, session, base_folder, bundleId, filename="file.pdf",contentType ="pdf",type="ORIGINAL"):
    
    # Step 4: Upload a file to a specific bundle
    url_step4 = f"{DSPACE_DOMAIN}:{DSPACE_PORT}/server/api/core/bundles/{bundleId}/bitstreams"

    headers_step4 = {
        "Authorization": bearer_token,
        "X-XSRF-TOKEN": xsrf_cookie_step3,
    }

    # Construct the full path to 'file.pdf'
    file_path = os.path.join(base_folder, f"{filename}")

    # Create multipart form data
    form_data = aiohttp.FormData()

    # Add file field with correct filename
    form_data.add_field('file', open(file_path, 'rb'), filename=f"{filename}", content_type=f"application/{contentType}")

    # Add properties as a JSON field
    properties = {
        "name": f"{filename}",
        "metadata": {
            "dc.description": [
                {
                    "value": "example file",
                    "language": None,
                    "authority": None,
                    "confidence": -1,
                    "place": 0
                }
            ]
        },
        "bundleName": f"{type}"
    }

    form_data.add_field('properties', json.dumps(properties), content_type='application/json')

    # Make the POST request with multipart/form-data
    async with session.post(url_step4, headers=headers_step4, data=form_data) as response_step4:
        # Print the response for Step 4
        result = {}
        
        result["response"] = await response_step4.json()
        result["msg"] = response_step4.status
            
        return result
