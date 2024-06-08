import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Redirect stdout and stderr to /dev/null
sys.stdout = open(os.devnull, 'w')
sys.stderr = open(os.devnull, 'w')

try:
    service = Service("chromedriver-win64/chromedriver.exe")
    options = Options()
    options.add_argument("--user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://web.whatsapp.com")
finally:
    # Restore stdout and stderr
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
