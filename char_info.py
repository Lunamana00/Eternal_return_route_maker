from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time
import copy
options = Options()
options.add_experimental_option('detach', True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])


def get_data():

    wd_char = webdriver.Chrome(options=options)
    wd_char.get("https://er.inven.co.kr/db/character")
    time.sleep(1)

    final_save = dict()

    links = wd_char.find_elements(By.CLASS_NAME,"layer_detail")
    char_info = open("char_info.txt","w")
    for i in range(int(len(links)/3)):
        temp_list = []
        link = links[3*i].get_attribute("href")
        
        char_info_wd = webdriver.Chrome(options=options)
        char_info_wd.get(link)
        time.sleep(2)
        charactor = char_info_wd.find_element(By.CLASS_NAME,'skinName').get_attribute("innerHTML")
        weapon_raw = char_info_wd.find_elements(By.CSS_SELECTOR,'div.skillTitle > span:nth-child(3)')
        
        for s in weapon_raw:
            temp_list.append(s.get_attribute("innerHTML")[9:-1])
            
        temp_list2 = copy.deepcopy(temp_list)
        final_save[charactor] = temp_list2

        char_info_wd.close()

    wd_char.close()

    for i in final_save.keys():
        char_info.write(i+"\n")

        for s in final_save[i]:
            char_info.writelines(s)
        char_info.write("\n")
    
    char_info.close()

get_data()