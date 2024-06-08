from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
def read_messages_from_file(file_path):
    with open(file_path, 'r') as file:
        messages = file.readlines()
    return [message.strip() for message in messages]
service = Service("chromedriver-win64/chromedriver.exe")
options = Options()
options.add_argument("--user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://web.whatsapp.com")
wait = WebDriverWait(driver, 20)
file_path = "chromedriver-win64/halmons.txt"
target_group_name = '//span[@title="Group name"]'
target_name_members = '//span[text()="Group name"]'
group_name = wait.until(EC.presence_of_element_located((By.XPATH, target_group_name)))
group_name.click()
group_name_members = wait.until(EC.presence_of_element_located((By.XPATH , )))
group_name_members.click()
message_box_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
message_box = wait.until(EC.presence_of_element_located((By.XPATH, message_box_path)))
messages = read_messages_from_file(file_path)
while True:
    for message in messages:
        message_box.send_keys(message + Keys.ENTER)

