import requests
from playwright import sync_playwright
from selenium import webdriver

import time
import csv

from login import login, login_selenium, chrome_driver_location

practice_manual_links = []

driver = webdriver.Chrome(chrome_driver_location)
login_selenium(driver)

for pm in practice_manual_links:
    driver.get(pm)
    name = driver.find_element_by_css_selector(".cle-pagetitle").text.replace(": ", "—")
    time.sleep(.5)

    list_items = []

    # Front Matter
    try:
        front_matter = driver.find_element_by_css_selector("#FM")
        open(name + '.html', 'a',
             encoding='utf-8').write('<div id="Front Matter" class="major">')
        front_matter.click()

        list_items = driver.find_elements_by_css_selector("#front-matter a")
        for item in list_items:
            time.sleep(.4)
            front_matter.click()
            title = item.get_attribute('title')
            item.click()
            innerHTML = driver.find_element_by_css_selector(
                "#main-content-inner").get_attribute('innerHTML')
            open(name + '.html', 'a', encoding='utf-8').write('<div title="' +
                                                              title + '" class="minor">')
            open(name + '.html', 'a', encoding='utf-8').write(innerHTML)
            open(name + '.html', 'a', encoding='utf-8').write('</div>')

        open(name + '.html', 'a', encoding='utf-8').write('</div>')
    except:
        pass

    # Chapters
    try:
        chapter = driver.find_element_by_css_selector("#C")
        open(name + '.html', 'a',
             encoding='utf-8').write('<div id="Chapters" class="major">')
        chapter.click()

        list_items = driver.find_elements_by_css_selector(
            "#treeWrapper>div>ul>li>a")
        for item in list_items:
            time.sleep(.4)
            chapter.click()
            title = item.text
            item.click()
            innerHTML = driver.find_element_by_css_selector(
                "#main-content-inner").get_attribute('innerHTML')
            open(name + '.html', 'a', encoding='utf-8').write('<div title="' +
                                                              title + '" class="minor">')
            open(name + '.html', 'a', encoding='utf-8').write(innerHTML)
            open(name + '.html', 'a', encoding='utf-8').write('</div>')

        open(name + '.html', 'a', encoding='utf-8').write('</div>')
    except:
        pass

    # Forms & Precedents
    try:
        fp = driver.find_element_by_css_selector("#FP")
        open(name + '.html', 'a',
             encoding='utf-8').write('<div id="Forms and Precedents" class="major">')
        fp.click()

        list_items = driver.find_elements_by_css_selector(
            "#forms-and-precedents a")
        for item in list_items:
            time.sleep(.4)
            fp.click()
            title = item.get_attribute('title')
            item.click()
            innerHTML = driver.find_element_by_css_selector(
                "#main-content-inner").get_attribute('innerHTML')
            open(name + '.html', 'a', encoding='utf-8').write('<div title="' +
                                                              title + '" class="minor">')
            open(name + '.html', 'a', encoding='utf-8').write(innerHTML)
            open(name + '.html', 'a', encoding='utf-8').write('</div>')

        open(name + '.html', 'a', encoding='utf-8').write('</div>')
    except:
        pass

    # Checklists
    try:
        cl = driver.find_element_by_css_selector("#CL")
        open(name + '.html', 'a',
             encoding='utf-8').write('<div id="Checklists" class="major">')
        cl.click()

        list_items = driver.find_elements_by_css_selector("#checklists a")
        for item in list_items:
            time.sleep(.4)
            cl.click()
            title = item.get_attribute('title')
            item.click()
            innerHTML = driver.find_element_by_css_selector(
                "#main-content-inner").get_attribute('innerHTML')
            open(name + '.html', 'a', encoding='utf-8').write('<div title="' +
                                                              title + '" class="minor">')
            open(name + '.html', 'a', encoding='utf-8').write(innerHTML)
            open(name + '.html', 'a', encoding='utf-8').write('</div>')

        open(name + '.html', 'a', encoding='utf-8').write('</div>')
    except:
        pass

    # Related Documents
    try:
        rd = driver.find_element_by_css_selector("#RD")
        open(name + '.html', 'a',
             encoding='utf-8').write('<div id="Related Documents" class="major">')
        rd.click()

        list_items = driver.find_elements_by_css_selector(
            "#related-documents a")
        for item in list_items:
            time.sleep(.4)
            rd.click()
            title = item.get_attribute('title')
            item.click()
            innerHTML = driver.find_element_by_css_selector(
                "#main-content-inner").get_attribute('innerHTML')
            open(name + '.html', 'a', encoding='utf-8').write('<div title="' +
                                                              title + '" class="minor">')
            open(name + '.html', 'a', encoding='utf-8').write(innerHTML)
            open(name + '.html', 'a', encoding='utf-8').write('</div>')

        open(name + '.html', 'a', encoding='utf-8').write('</div>')
    except:
        pass
