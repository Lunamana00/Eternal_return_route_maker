import os

def data_replace(a):
    char_list = os.listdir(a)
    for  i in char_list:
        os.rename(a+i,a+i[:-3]+".png")

data_replace("./char_img/")
data_replace("./f_item_img/")
data_replace("./matarial_img/")