import requests
from playwright import sync_playwright
from selenium import webdriver

import time
import csv

from login import login, login_selenium, chrome_driver_location


precedents = open('list_of_precedent_links.txt', 'r') 
lines = precedents.readlines()
  
set_lines = sorted(list(set(lines)))

with open('list_of_unique_precedent_links.txt', 'w') as precedents:
  for line in set_lines:
    precedents.write(line)
