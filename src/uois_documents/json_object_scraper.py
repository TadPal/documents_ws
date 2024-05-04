from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from time import sleep
import base64
import json
import os

from selenium.webdriver.common.action_chains import ActionChains


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

    # login
    field = driver.find_element(By.NAME, "UserName")
    field.clear()
    field.send_keys(base64.b64decode(username).decode("utf-8"))
    sleep(1)

    field = driver.find_element(By.NAME, "Password")
    field.clear()
    field.send_keys(base64.b64decode(password).decode("utf-8"))
    sleep(1)

    field = driver.find_element(By.ID, "submitButton")
    field.click()
    sleep(1)


    # getting into element folder
    elements = driver.find_elements(By.CLASS_NAME, 'ms-Link')

    for i in range(0, len(elements)):
        sleep(1)

        # Re-find elements
        elements = driver.find_elements(By.CLASS_NAME, 'ms-Link')  
        element = elements[i]

        # Click on element
        action = ActionChains(driver)
        action.move_to_element(element).click().perform()

        sleep(1)
        driver.back()



    driver.back()
    # field = driver.find_element(By.TAG_NAME, "Pre")
    # assert type(field.text) == str
    # json_object = json.loads(field.text)
    # json_object = json.dumps(json_object, indent=4)

    # with open(output_file, "x") as f:
    #     f.write(json_object)

    # driver.close()


# pass credentials
with open("secret/passwords.json") as f:
    data = json.load(f)
    USERNAME = data["user"]["name"]
    PASSWD = data["user"]["pass"]

    #pass url
    with open("secret/url.json") as u:
        urlData = json.load(u)
        url = urlData["url_pred_symsmt"]

        output_file = find_file_name()
        scrape_n_save(output_file, url, USERNAME, PASSWD)
