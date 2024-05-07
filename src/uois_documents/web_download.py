from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from time import sleep
import base64


def scrape_n_save(url, username, password, downloads_folder=""):
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": downloads_folder,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
        },
    )
    driver = webdriver.Chrome(options=options)

    def login():
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

    def search_files(elements):
        if len(elements) > 0:
            for i in range(len(elements)):
                element = elements[i]
                file_url = element.get_attribute("href")

                # Check if element is file or folder
                if "sourcedoc" not in file_url:
                    # Search the folder
                    element.click()
                    sleep(0.5)
                    subelements = driver.find_elements(By.CLASS_NAME, "ms-Link")
                    search_files(subelements)
                    driver.back()
                else:
                    # Open file tab
                    element.click()
                    sleep(2)

                    # Switch to the file tab
                    print(driver.window_handles)
                    driver.switch_to.window(driver.window_handles[-1])

                    # Switch to iframe and click the download button
                    driver.switch_to.frame("WebApplicationFrame")
                    driver.find_element(By.ID, "btnDownloadPdf-Medium20").click()
                    sleep(1)

                    # Switch back to the main tab
                    driver.switch_to.window(driver.window_handles[-1])
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])

                # Refresh elements
                elements = driver.find_elements(By.CLASS_NAME, "ms-Link")

    # Open URL and login
    driver.get(url)
    login()

    # Find all folders and files
    elements = driver.find_elements(By.CLASS_NAME, "ms-Link")
    search_files(elements)

    # End session
    sleep(5)
    driver.close()
