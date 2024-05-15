import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import os
import stat


def fill_google_form(work_done):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Path to the ChromeDriver
    chrome_driver_path = os.path.join('drivers', 'chromedriver')

    # Ensure the ChromeDriver is executable
    st = os.stat(chrome_driver_path)
    os.chmod(chrome_driver_path, st.st_mode | stat.S_IEXEC)

    # Initialize the Chrome driver
    service = Service(executable_path=chrome_driver_path)
    web = webdriver.Chrome(service=service, options=chrome_options)

    web.get('https://forms.gle/eeGSVR2UojvDpFTYA')
    time.sleep(2)

    name = web.find_element(By.XPATH,
                            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name.send_keys("Mustkeem Baraskar")

    today_date = datetime.now().strftime("%d-%m-%Y")
    date_entry = web.find_element(By.XPATH,
                                  '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
    date_entry.send_keys(today_date)

    workdone = web.find_element(By.XPATH,
                                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    workdone.send_keys(work_done)

    location = web.find_element(By.XPATH,
                                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    location.send_keys("Office")

    status = web.find_element(By.XPATH,
                              '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    status.send_keys("Present")

    submit_button = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

    time.sleep(1)


st.title("Google Form Filler")

work_done = st.text_area("Enter Work Done:")
if st.button("Submit"):
    fill_google_form(work_done)
    st.success("Form Submitted Successfully!")
