import requests
from playwright import sync_playwright
from selenium import webdriver

import time
import csv

from login import login, login_selenium, chrome_driver_location



driver = webdriver.Chrome(chrome_driver_location)
login_selenium(driver)

precedents = open('list_of_unique_precedent_links.txt', 'r') 
lines = precedents.readlines() 
  
for line in lines:
  url = line.strip()
  driver.get(url)

  # Download doc file
  download = driver.find_element_by_css_selector("#ops-document-formats a")
  download.click()

  # Note down metadata
  metadata = driver.find_element_by_css_selector("#ops-doc-info").get_attribute('innerHTML')
  try:
    preview = driver.find_element_by_css_selector(".WordSection1").get_attribute('innerHTML')
  except:
    try:
      preview = driver.find_element_by_css_selector(".Section1").get_attribute('innerHTML')
    except:
      preview = ""

  metadata = metadata.replace("\t", "").replace("\r", "").replace("\n", "")
  preview = preview.replace("\t", "").replace("\r", "").replace("\n", "")

  name = driver.find_element_by_css_selector("#ops-addnew").text.replace("\t", "").replace("\r", "").replace("\n", "")

  with open('precedent_files.csv', 'a', encoding='utf-8', newline='\n') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow((name, url, preview, metadata))
  time.sleep(1)


# TODO: Separate scrape the index to organize files



# precedents = open('list_of_precedent_links.txt', 'r') 
# lines = precedents.readlines() 
  
# for line in lines[0:2]:
#   url = line.strip()
#   r = requests.get('https://pc.cle.bc.ca/clebc-pc-web/document.do?fpid=4357&format=DOC', allow_redirects=True)
#   open('sample.doc', 'wb').write(r.content)
#   print(r.headers.get('content-type'))






# with sync_playwright() as p:
#   browser = p.chromium.launch(headless=False)
#   page = browser.newPage()
#   login(page)

#   precedents = open('list_of_precedent_links.txt', 'r') 
#   lines = precedents.readlines() 
    
#   for line in lines[0:2]:
#     url = line.strip()
#     page.goto(url)
#     page.click('#ops-document-formats a')
#     page.waitForTimeout(1000000)



  # page.goto('https://google.com')
  # browser.close()
