from web_download import scrape_n_save
import json

if __name__ == "__main__":
    with open("secret/passwords.json") as f:
        data = json.load(f)
        USERNAME = data["user"]["name"]
        PASSWD = data["user"]["pass"]
        DOWNLOADS = data["downloads_folder"]

        # pass url
        with open("secret/url.json") as u:
            links = json.load(u)
            for link in links:
                URL = link["url"]
                scrape_n_save(
                    url=URL,
                    username=USERNAME,
                    password=PASSWD,
                    downloads_folder=DOWNLOADS,
                )