from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from time import sleep
import base64
import json
import os


def find_file_name():
    file_name = ""
    dir_list = os.listdir("scraped")
    file_number = int(dir_list[-1].split("_")[-1].split(".")[0]) + 1
    file_name = f"scraped/object_{file_number}.json"
    return file_name


def scrape_n_save(output_file, url, username, password):
    driver = webdriver.Firefox()
    driver.get(url)
    sleep(1)

    alert = Alert(driver)
    alert.dismiss()
    sleep(1)

    driver.refresh()
    assert "UoD" in driver.title

    field = driver.find_element(By.NAME, "Username")
    field.clear()
    field.send_keys(base64.b64decode(username).decode("utf-8"))
    sleep(1)

    field = driver.find_element(By.NAME, "Password")
    field.clear()
    field.send_keys(base64.b64decode(password).decode("utf-8"))
    sleep(1)

    field = driver.find_element(By.XPATH, "//button[@value='login']")
    field.click()
    sleep(10)

    field = driver.find_element(By.TAG_NAME, "Pre")
    assert type(field.text) == str
    json_object = json.loads(field.text)
    json_object = json.dumps(json_object, indent=4)

    with open(output_file, "x") as f:
        f.write(json_object)

    driver.close()


with open("secret/passwords.json") as f:
    data = json.load(f)
    USERNAME = data["user"]["name"]
    PASSWD = data["user"]["pass"]
    url = "https://apl.unob.cz/rozvrh/api/read/rozvrh?id=7"
    output_file = find_file_name()
    scrape_n_save(output_file, url, USERNAME, PASSWD)
