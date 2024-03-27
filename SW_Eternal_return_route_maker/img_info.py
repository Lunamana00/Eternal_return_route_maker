from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time
import re
import os
import urllib.request

options = Options()
options.add_experimental_option('detach', True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

def char_data():

    char_img = webdriver.Chrome(options=options)
    char_img.get("https://er.inven.co.kr/db/character")
    time.sleep(1)

    if not os.path.exists("./char_img"):
        os.makedirs("./char_img")

    for i in range(1,70):
        img = char_img.find_element(By.CSS_SELECTOR," div > div:nth-child("+str(i)+") > div.db_block.card_img > a:nth-child(2) > img").get_attribute("src")
        img_name = char_img.find_element(By.CSS_SELECTOR,"div > div:nth-child("+str(i)+") > div.db_block.card_info > p > a:nth-child(2)").get_attribute("innerHTML")
        f = open("./char_img/"+img_name+".jpg",'wb')
        f.write(urllib.request.urlopen(img).read())
        f.close()

    char_img.close()

def item_data():

    item_img = webdriver.Chrome(options=options)
    item_img.get("https://er.inven.co.kr/db/item#r4c3")
    time.sleep(1)

    if not os.path.exists("./f_item_img"):
        os.makedirs("./f_item_img")

    for i in range(1,185):
        img = item_img.find_element(By.CSS_SELECTOR,"table > tbody > tr:nth-child("+str(i)+") > td.option_text.txt_center > span > a > span > img").get_attribute("src")
        img_name = item_img.find_element(By.CSS_SELECTOR,"table > tbody > tr:nth-child("+str(i)+") > td:nth-child(2) > span > a").get_attribute("innerHTML")
        f = open("./f_item_img/"+img_name+".jpg",'wb')
        f.write(urllib.request.urlopen(img).read())
        f.close()

    item_img.close()

def matarial_data():

    matarial_img = webdriver.Chrome(options=options)
    matarial_img.get("https://er.inven.co.kr/db/item#r4c0")
    time.sleep(1)

    if not os.path.exists("./matarial_img"):
        os.makedirs("./matarial_img")

    for i in range(1,85):
        img = matarial_img.find_element(By.CSS_SELECTOR,"table > tbody > tr:nth-child("+str(i)+") > td.option_text.txt_center > span > a > span > img").get_attribute("src")
        img_name = matarial_img.find_element(By.CSS_SELECTOR,"table > tbody > tr:nth-child("+str(i)+") > td:nth-child(2) > span > a").get_attribute("innerHTML")
        f = open("./matarial_img/"+img_name+".jpg",'wb')
        f.write(urllib.request.urlopen(img).read())
        f.close()

    matarial_img.close()

matarial_data()
