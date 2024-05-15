import streamlit as st
from selenium import webdriver
import time
from datetime import datetime

def fill_google_form(work_done):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    web = webdriver.Chrome(options=chrome_options)
    web.get('https://forms.gle/eeGSVR2UojvDpFTYA')
    time.sleep(2)

    name = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name.send_keys("Mustkeem Baraskar")

    today_date = datetime.now().strftime("%d-%m-%Y")
    date_entry = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
    date_entry.send_keys(today_date)

    workdone = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    workdone.send_keys(work_done)

    location = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    location.send_keys("Office")

    status = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    status.send_keys("Present")

    submit_button = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

    time.sleep(1)

st.title("Google Form Filler")

work_done = st.text_area("Enter Work Done:")
if st.button("Submit"):
    fill_google_form(work_done)
    st.success("Form Submitted Successfully!")
