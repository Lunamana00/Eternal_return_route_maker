from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time
import re

options = Options()
options.add_experimental_option('detach', True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])


def get_data():

    wd_item = webdriver.Chrome(options=options)
    wd_item.get("https://er.inven.co.kr/db/item#r4c3")
    time.sleep(1)

    item_info = dict()

    for i in range(1,185):

        item_name = wd_item.find_element(By.CSS_SELECTOR, "tbody > tr:nth-child("+str(i)+") > td:nth-child(2) > span > a").get_attribute('innerHTML')
        
        item_case = wd_item.find_element(By.CSS_SELECTOR, "tbody > tr:nth-child("+str(i)+") > td.class2text.txt_center > span").get_attribute('innerHTML')
        
        if item_case != "재료":

            item_option = wd_item.find_elements(By.CLASS_NAME,"option_text")
            item_option = item_option[3*i-1].get_attribute('innerHTML')
            p = re.compile('(?=>)(.*?)(?=<)')
            p_list = p.findall(item_option)

            for s in range(len(p_list)):

                p_list[s] = p_list[s][1:]
            
            item_option = p_list

            if '(고유)' in item_option:
                item_option.pop(item_option.index('(고유)'))

            item_option = list(filter(None, item_option))
        
        else:
            item_option = ['재료']


        item_matarial_adress = wd_item.find_element(By.CSS_SELECTOR,"tbody > tr:nth-child("+str(i)+") > td:nth-child(2) > span > a").get_attribute('href')
        mat_ad = webdriver.Chrome(options=options)
        mat_ad.get(item_matarial_adress)
        item_matarial_list = mat_ad.find_elements(By.CLASS_NAME,"itemname")
        item_matarial_core = []

        for t in item_matarial_list:

            if t.get_attribute('data-color-itemgrade') == "1":
                item_matarial_core.append(t.get_attribute("innerHTML"))

        mat_ad.close()

        item_info[item_name] =([item_case , item_option , item_matarial_core])
    

    f_if = open("item_info.txt","w")

    for i in item_info.keys():
        f_if.write(i+"\n")
        
        for s in item_info[i]:
            f_if.write(str(s)+" ")
            f_if.write("\n")
        
    f_if.close


def item_locate():

    base_item_dv = webdriver.Chrome(options=options)
    base_item_dv.get("https://er.inven.co.kr/db/item#r4c0")
    time.sleep(1)

    base_item_dict = dict()

    for i in range(1,85):
        base_item = base_item_dv.find_element(By.CSS_SELECTOR,"tr:nth-child("+str(i)+") > td:nth-child(2) > span > a").get_attribute("innerHTML")
        base_item_loc = base_item_dv.find_element(By.CSS_SELECTOR,"tr:nth-child("+str(i)+") > td:nth-child(5) > span").get_attribute("innerHTML")
        
        p = re.compile('(?=발견 장소)(.*?)(?=<)')
        q = re.compile('(?<= )(.*?)(?=\()')
        r = re.compile("'([^']+)'")
        base_item_loc_1st = p.findall(base_item_loc)
        base_item_loc_2nd = str(q.findall(str(base_item_loc_1st))).replace("장소: ","")
        base_item_loc_3rd = r.findall(base_item_loc_2nd)

        base_item_dict[base_item] = base_item_loc_3rd

    base_item_dv.close()

    f_bid = open("base_item_dict.txt","w")

    for i in base_item_dict.keys():
        f_bid.write(i+"\n")

        for s in base_item_dict[i]:
            f_bid.write(s+" ")
        f_bid.write("\n")
        
    f_bid.close


get_data()
item_locate()

            



    

