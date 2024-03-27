from tkinter import *
import tkinter.font
from main import *
from functools import partial
import os
import re
from tkinter.tix import *
from PIL import Image, ImageTk

class Char_bt:

    def __init__(self, name, pngname, button):

        self.name = name
        self.pngname = pngname
        self.button = button

class Weapon_bt2:

    def __init__(self,name,options,img,func,button,label,blank):

        self.name = name
        self.options = options
        self.img = img
        self.func = func
        self.button = button
        self.label = label
        self.blank = blank

class Weapon_bt:

    def __init__(self, name, partialfunc, button, blank):

        self.name = name
        self.partialfunc = partialfunc
        self.button = button
        self.blank = blank

class F_route:

    def __init__(self, route_num, buy_mat, mat_img, buy_num, item, item_img,route, col_option, btn) :
        
        self.route_num = route_num
        self.buy_mat = buy_mat
        self.mat_img = mat_img
        self.buy_num = buy_num
        self.item = item
        self.item_img = item_img
        self.route = route
        self.col_option = col_option
        self.btn = btn

class F_item_option:
    #ap, lvap, ad, lvad, ats, arp, hp, lvhp, ar, cd
    def __init__(self, name):

        self.name = name
        self.ap = 0
        self.lvap = ""
        self.ad = 0
        self.lvad = ""
        self.ats = 0
        self.arp = 0
        self.hp = 0
        self.lvhp = ""
        self.ar = 0
        self.cd = 0

class f_obj:

    def __init__(self,
                 item1_img,item2_img, item3_img, item4_img,item5_img,
                 item1,item2,item3,item4,item5,
                 mat, mat_img, mat_num,
                 options,route,btn):

        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
        self.item4 = item4
        self.item5 = item5
        self.item1_img = item1_img
        self.item2_img = item2_img
        self.item3_img = item3_img
        self.item4_img = item4_img
        self.item5_img = item5_img
        self.mat = mat
        self.mat_img = mat_img
        self.mat_num = mat_num
        self.options = options
        self.route = route
        self.btn = btn


def start():

    global matarial_dict, item_info_dict, char_info_dict

    matarial_dict, item_info_dict, char_info_dict = setting()

    Char_choice()
    

def Char_choice():
    global Char_Frame

    char_list = os.listdir("./char_img")

    btname_dict = dict()

    for i in char_list:
        btname_dict[i[:-4]] = Char_bt(i[:-4],"./char_img/"+i, "")

    Main.destroy()

    Char_Frame = Tk()
    Char_Frame.title("ETERNAL RETURN ROOT MAKER")
    Char_Frame.geometry("+0+0")

    x_count = 0
    y_count = 0
    count = 0

    photo_list = []
    partial_list = []
    name_list = []

    for i in btname_dict:
        photo_list.append(PhotoImage(file=str(btname_dict[i].pngname)).subsample(2,2))
        partial_list.append(partial(Weapon_choice,(btname_dict[i].name)))
        name_list.append(btname_dict[i].name)

    for i in btname_dict:

        btname_dict[i].button = Button(Char_Frame, height=60, width=50, overrelief="solid", command=partial_list[count]
                                       ,image=photo_list[count])

        btname_dict[i].button.grid(row=y_count*111,column =x_count*111)

        count += 1
        if x_count == 8:
            x_count = 0
            y_count += 1
        else:
            x_count += 1
        if count == 68:
            break

    Char_Frame.mainloop()

def Weapon_choice(name):

    global Weapon_Frame, char_name
    
    Char_Frame.destroy()

    char_name = name

    Weapon_Frame=Tk()
    Weapon_Frame.title("ETERNAL RETURN ROOT MAKER")
    Weapon_Frame.geometry("+0+0")
    
    photo = PhotoImage(file="./char_img/"+name+".png")
    null_1 = Label(Weapon_Frame,text="  ",height=2)
    null_1.pack()

    font = tkinter.font.Font(size =15,weight="bold")
    announce = Label(Weapon_Frame,text="       [무기 종류를 선택해 주세요]       ",font=font)
    announce.pack()
    pic = Label(Weapon_Frame,image=photo,height=250,width=250)
    pic.pack()
    

    weapon_bt_dict = dict()

    for i in char_info_dict[name].weapon:
        weapon_bt_dict[i] = Weapon_bt(i,partial(Weapon_choice2, i),"","")

    for i in weapon_bt_dict.keys():
        weapon_bt_dict[i].button = Button(Weapon_Frame,overrelief="solid", text=i, 
                          font=font, command=weapon_bt_dict[i].partialfunc)
        weapon_bt_dict[i].button.pack()
        weapon_bt_dict[i].blank = Label(Weapon_Frame,text="      ")
        weapon_bt_dict[i].blank.pack()

    null_2 = Label(Weapon_Frame, text="  ",height=3)
    null_2.pack()

    Weapon_Frame.mainloop()

def Weapon_choice2(weapon):

    global weapon_list, head_list, clothes_list, arm_list, leg_list,Weapon_Frame2

    Weapon_Frame.destroy()

    weapon_list, head_list, clothes_list, arm_list, leg_list = choose_item(char_name,weapon)

    Weapon_Frame2=Tk()
    Weapon_Frame2.title("ETERNAL RETURN ROOT MAKER")
    Weapon_Frame2.geometry("+0+0")

    null_1 = Label(Weapon_Frame2,text="  ",height=3)
    null_1.pack()

    font = tkinter.font.Font(size = 30,weight="bold")
    font3 = tkinter.font.Font(size = 15,weight="bold")
    font2 = tkinter.font.Font(size = 10,weight="bold")
    announce = Label(Weapon_Frame2,text="          [무기를 선택해 주세요]          ",font=font3)
    announce.pack()

    null_2 = Label(Weapon_Frame2, text="  ",height=2)
    null_2.pack()

    weapon_bt2_dict = dict()

    for i in weapon_list:
        weapon_bt2_dict[i.name] = Weapon_bt2(i.name,i.options,PhotoImage(file="./f_item_img/"+i.name+".png"),partial(buy_num,i.name),"","","")
    
    for i in weapon_bt2_dict.keys():
        weapon_bt2_dict[i].button = Button(Weapon_Frame2,overrelief="solid",image=weapon_bt2_dict[i].img,command=weapon_bt2_dict[i].func)
        weapon_bt2_dict[i].button.pack()
        weapon_bt2_dict[i].label = Label(Weapon_Frame2,text=i,font=font2)
        weapon_bt2_dict[i].label.pack()
        weapon_bt2_dict[i].options = Label(Weapon_Frame2,text=weapon_bt2_dict[i].options)
        weapon_bt2_dict[i].options.pack()
        weapon_bt2_dict[i].blank = Label(Weapon_Frame2,text="")
        weapon_bt2_dict[i].blank.pack()

    null_3 = Label(Weapon_Frame2, text="  ",height=2)
    null_3.pack()

    Weapon_Frame2.mainloop()

def buy_num(weapon):

    global Buy_num

    Weapon_Frame2.destroy()

    Buy_num=Tk()
    Buy_num.title("ETERNAL RETURN ROOT MAKER")
    Buy_num.geometry("+0+0")
    Buy_num.resizable(False,False)

    null_1 = Label(Buy_num,text="  ",height=3)
    null_1.grid(row=0,column=0)

    font = tkinter.font.Font(size = 15,weight="bold")
    font2 = tkinter.font.Font(size = 10,weight="bold")

    announce = Label(Buy_num,text="[구매할 최대 재료 수를 정해주세요]",font=font)
    announce.grid(row=1,column=2)

    null_2 = Label(Buy_num,text="  ",height=3)
    null_2.grid(row=2,column=3)

    null_3 = Label(Buy_num,text="  ",height=3,width=10)
    null_3.grid(row=3,column=0)

    bt0_cmd = partial(route_define,weapon,0)
    bt0 = Button(Buy_num,text="0 개",font=font2,command=bt0_cmd,width=5)
    bt0.grid(row=3,column=1,sticky="e")
    bt1_cmd = partial(route_define,weapon,1)
    bt1 = Button(Buy_num,text="1 개",font=font2,command=bt1_cmd,width=5)
    bt1.grid(row=3,column=2)
    bt2_cmd = partial(route_define,weapon,2)
    bt2 = Button(Buy_num,text="2 개",font=font2,command=bt2_cmd,width=5)
    bt2.grid(row=3,column=3,sticky="w")

    null_4 = Label(Buy_num,text="  ",height=3,width=10)
    null_4.grid(row=3,column=4)

    null_3 = Label(Buy_num,text="  ",height=3)
    null_3.grid(row=4,column=0)

    Buy_num.mainloop()

def col_item_option(item):

    global F_item_dict, F_item_option

    F_item_dict = dict()

    for i in item:
        for s in i:
            F_item_dict[s.name] = F_item_option(s.name)
            for t in s.options:
                if "스킬 증폭 +" in t[:8]:
                    F_item_dict[s.name].ap = int(t[7:])                
                if "레벨 당 스킬 증폭 +" in t:
                    F_item_dict[s.name].lvap = t
                if "공격력 +" in t[:6]:
                    F_item_dict[s.name].ad = int(t[5:])
                if "레벨 당 공격력 +" in t:
                    F_item_dict[s.name].lvad = t
                if "공격 속도 +" in t[:8]:
                    F_item_dict[s.name].ats = int(t[7:-1])
                if "방어 관통 +" in t:
                    if t[-1] == "%":
                        F_item_dict[s.name].arp = int(t[7:-1])
                    else:
                        F_item_dict[s.name].arp = int(t[7:])
                if "최대 체력 +" in t[:8]:
                    F_item_dict[s.name].hp = int(t[7:])
                if "레벨 당 최대 체력 +" in t:
                    F_item_dict[s.name].lvhp = t
                if "방어력 +" in t:
                    F_item_dict[s.name].ar = int(t[5:])
                if "쿨다운 감소 +" in t:
                    F_item_dict[s.name].cd = int(t[8:-1])

def final_info(buy_item, buy_num, item, route):

    f_route_dict = dict()

    for i in range(len(buy_item)):
        mat_photo_list = []
        for s in buy_item[i]:
            mat_photo_list.append(PhotoImage(file="./matarial_img/"+s+".png").subsample(2,2))
        
        item_photo_list = []
        item_list = []

        ap = 0
        lvap = ""
        ad = 0
        lvad = ""
        ats = 0
        arp = 0
        hp = 0
        lvhp = ""
        ar = 0
        cd =0

        for s in item[i]:
            item_photo_list.append(PhotoImage(file="./f_item_img/"+s.name+".png").subsample(2,2))

            item_list.append(s.name)
            ap += F_item_dict[s.name].ap
            lvap += F_item_dict[s.name].lvap
            ad += F_item_dict[s.name].ad
            lvad += F_item_dict[s.name].lvad
            ats += F_item_dict[s.name].ats
            arp += F_item_dict[s.name].arp
            hp += F_item_dict[s.name].hp
            lvhp += F_item_dict[s.name].lvhp
            ar += F_item_dict[s.name].ar
            cd += F_item_dict[s.name].cd

        f_route_dict[i] = F_route(i,buy_item[i],mat_photo_list,buy_num[i],
                                  item_list,item_photo_list,route[i],
                                  F_item_option(i),"")
        
        f_route_dict[i].col_option.ap = ap
        f_route_dict[i].col_option.lvap = lvap
        f_route_dict[i].col_option.ad = ad
        f_route_dict[i].col_option.lvad = ad
        f_route_dict[i].col_option.ats = ats
        f_route_dict[i].col_option.arp = arp
        f_route_dict[i].col_option.hp = hp
        f_route_dict[i].col_option.lvhp = lvhp
        f_route_dict[i].col_option.ar = ar
        f_route_dict[i].col_option.cd = cd

    return f_route_dict

def route_define(weapon,num):

    global root

    Buy_num.destroy() 

    buy_item, buy_num, item, route = item_loop(weapon,num)

    root = Tk()
    root.title("ETERNAL RETURN ROOT MAKER")
    root.geometry("+0+0")
    canvas = Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", on_mousewheel)
    canvas.update()
    canvas.config(scrollregion=canvas.bbox("all"))

    route_define_Frame = Frame(canvas)
    canvas.create_window((0, 0), window=route_define_Frame, anchor="nw")

    def resize_canvas(event):
        new_height = min(800, event.height)

        canvas.config(width=event.width, height=new_height)

        canvas.config(scrollregion=canvas.bbox("all"))

    route_define_Frame.bind("<Configure>", resize_canvas)
    
    col_item_option(item)

    photo = PhotoImage(file="./go.png")
    photo = photo.subsample(8,8)
    

    f_route_dict = final_info(buy_item, buy_num, item, route)

    obj_dict = dict()
    max_len = 0
    for i in f_route_dict.keys():
        
        if max_len <= len(f_route_dict[i].route):
            max_len = len(f_route_dict[i].route)

    for i in f_route_dict.keys():

        obj_dict[i] = f_obj("a1","a2","a3","a4","a5",
                            "b1","b2","b3","b4","b5",
                            "mat","mat_img","mat_num",
                            "option","route","btn")

        font = tkinter.font.Font(size = 15,weight="bold")
        font1 = tkinter.font.Font(size = 12,weight="bold")
        font2 = tkinter.font.Font(size = 7,weight="bold")
        

        obj_dict[i].item1_img = Label(route_define_Frame, image=f_route_dict[i].item_img[0], relief="solid")
        obj_dict[i].item2_img = Label(route_define_Frame, image=f_route_dict[i].item_img[1], relief="solid")
        obj_dict[i].item3_img = Label(route_define_Frame, image=f_route_dict[i].item_img[2], relief="solid")
        obj_dict[i].item4_img = Label(route_define_Frame, image=f_route_dict[i].item_img[3], relief="solid")
        obj_dict[i].item5_img = Label(route_define_Frame, image=f_route_dict[i].item_img[4], relief="solid") 
        
        obj_dict[i].item1 = Label(route_define_Frame, text=f_route_dict[i].item[0],font = font2)
        obj_dict[i].item2 = Label(route_define_Frame, text=f_route_dict[i].item[1],font = font2)
        obj_dict[i].item3 = Label(route_define_Frame, text=f_route_dict[i].item[2],font = font2)
        obj_dict[i].item4 = Label(route_define_Frame, text=f_route_dict[i].item[3],font = font2)
        obj_dict[i].item5 = Label(route_define_Frame, text=f_route_dict[i].item[4],font = font2)

        item_list_img = [obj_dict[i].item1_img,obj_dict[i].item2_img,obj_dict[i].item3_img,obj_dict[i].item4_img,obj_dict[i].item5_img]           
        item_list_name = [obj_dict[i].item1,obj_dict[i].item2,obj_dict[i].item3,obj_dict[i].item4,obj_dict[i].item5]
        
        count = 1

        for s in range(5):
            Label(route_define_Frame, text=i+1,font=font).grid(row = 2*i,column= 0)
            item_list_img[s].grid(row = 2*i,column= count)
            item_list_name[s].grid(row = 2*i+1,column= count)
            count+=1
        
        option_arg = f_route_dict[i].col_option
        option_str = f"스킬 증폭:{option_arg.ap} 공격력:{f_route_dict[i].col_option.ad} 공격 속도:{f_route_dict[i].col_option.ats}% 방어 관통:{f_route_dict[i].col_option.arp} \n 체력:{f_route_dict[i].col_option.hp} 방어력:{f_route_dict[i].col_option.ar} 쿨타임 감소:{f_route_dict[i].col_option.cd}%"

        obj_dict[i].options = Label(route_define_Frame, text=option_str, font=font2, relief="sunken")
        obj_dict[i].options.grid(row = 2*i,column=6)

        Label(route_define_Frame, text="구매\n재료",relief="solid",font=font2).grid(row = 2*i,column= 7)

        obj_dict[i].mat_img = f_route_dict[i].mat_img
        obj_dict[i].mat = f_route_dict[i].buy_mat
        
        count = 0
        for s in range(len(obj_dict[i].mat_img)):
            Label(route_define_Frame, image=obj_dict[i].mat_img[s],relief="solid").grid(row = 2*i,column= 8+count)
            Label(route_define_Frame, text=obj_dict[i].mat[s],font = font2).grid(row = 2*i+1,column= 8+count)
            count+=1

        route_pass = partial(open_map,f_route_dict[i].route)
        font3 = tkinter.font.Font(size = 20,weight="bold")
        Label(route_define_Frame, text=f"{len(f_route_dict[i].route)} 루트",relief="solid",font=font1).grid(row = 2*i,column= 8+max_len)
        Label(route_define_Frame, text=f"{(f_route_dict[i].route)}",font=font2).grid(row = 2*i,column= 9+max_len)    
        Button(route_define_Frame,image=photo,command = route_pass).grid(row = 2*i,column= 10+max_len)
    
    root.mainloop()   

def open_map(route):
    root.destroy()

    Map_Frame = Tk()
    Map_Frame.title("ETERNAL RETURN ROOT MAKER")
    Map_Frame.geometry("+0+0")

    canvas = Canvas(Map_Frame, relief="solid", bd=2)
    canvas.pack()
    
    image_path = "./map.png"

    img = Image.open(image_path)
    img_width, img_height = img.size
    canvas.image = ImageTk.PhotoImage(img.resize((img.width // 2, img.height // 2)))

    canvas.config(width=img_width//2, height=img_height//2)

    canvas.create_image(0, 0, anchor="nw", image=canvas.image)

    x_y_loc = dict()
    
    x_y_loc["성당"] = [270, 371]
    x_y_loc["묘지"] = [321, 337]
    x_y_loc["공장"] = [368, 395]
    x_y_loc["병원"] = [382, 294]
    x_y_loc["연못"] = [306, 240]
    x_y_loc["개울"] = [356, 234]
    x_y_loc["절"] = [369, 150]
    x_y_loc["경찰서"] = [302, 154]
    x_y_loc["소방서"] = [259, 195]
    x_y_loc["골목길"] = [253, 86]
    x_y_loc["주유소"] = [199, 108]
    x_y_loc["학교"] = [188, 195]
    x_y_loc["양궁장"] = [130, 146]
    x_y_loc["호텔"] = [117, 241]
    x_y_loc["숲"] = [192, 311]
    x_y_loc["모래사장"] = [102, 314]
    x_y_loc["고급주택가"] = [162, 383]
    x_y_loc["창고"] = [222, 427]
    x_y_loc["항구"] = [274, 447]

    for i in route:
        x = x_y_loc[i][0]
        y = x_y_loc[i][1]

        canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="yellow")

    def on_canvas_click(event):

        global prev_x, prev_y
        prev_x, prev_y = event.x, event.y

    def on_canvas_drag(event):
        global prev_x, prev_y
        x, y = event.x, event.y
        canvas.create_line(prev_x, prev_y, x, y, fill="red", width=10)
        prev_x, prev_y = x, y

    def on_canvas_release(event):
        global prev_x, prev_y
        prev_x, prev_y = None, None

    canvas.bind("<Button-1>", on_canvas_click)
    canvas.bind("<B1-Motion>", on_canvas_drag)
    canvas.bind("<ButtonRelease-1>", on_canvas_release)

        
Main = Tk()
Main.title("ETERNAL RETURN ROOT MAKER")
Main.geometry("+0+0")

image = Image.open("./ER.png")
start_img = ImageTk.PhotoImage(image)
main_font = tkinter.font.Font(size = 20,weight="bold")
start_bt = Button(Main, overrelief="solid", command=start, compound="top", image=start_img,text="PRESS THE WINDOW",font=main_font)
start_bt.pack()

Main.mainloop()