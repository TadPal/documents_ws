import requests

def download_file(url, token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open('downloaded_document.pdf', 'wb') as f:
            f.write(response.content)
        print("File downloaded successfully!")
    else:
        print(f"Failed to download file: {response.status_code}")

# Replace these variables with your actual data
url = "URL_TO_YOUR_DOCUMENT"
token = "YOUR_AUTH_TOKEN"

download_file(url, token)
