import re
import copy

class Item:

    def __init__(self, name, type, options, matarial):
        
        self.name = name
        self.type = type
        self.options = options
        self.matarial = matarial

class Charactor:

    def __init__(self, name, weapon, power):

        self.name = name
        self.weapon = weapon
        self.power = power

##########################################################################################

def setting():
    
    global Item, Charactor, matarial_dict, item_info_dict, char_info_dict

    base_item = open("base_item_dict.txt","r")
    base_item_r = base_item.readlines()
    r_name = re.compile("(?=\D)(.*?)\n")
    r_place = re.compile("(?=\D)(.*?)\W")

    matarial_dict = dict()

    for i in range(int(len(base_item_r)/2)):        
        matarial_dict[r_name.findall(base_item_r[2*i])[0]] = r_place.findall(base_item_r[2*i+1][:-1])
    
    base_item.close()

    item_info = open("item_info.txt","r")
    item_info_r = item_info.readlines()

    item_info_dict = dict()

    i_name = re.compile("(?=\w)(.*?)\n")
    i_type = re.compile("(?=\w)(.*?) \n")
    i_options = re.compile("(?=\w)(.*?)\'")

    for i in range(int(len(item_info_r)/4)):
        
        item_name = i_name.findall(item_info_r[4*i])[0]
        item_type = i_type.findall(item_info_r[4*i+1])[0]
        item_options = i_options.findall(item_info_r[4*i+2])
        item_matarial = i_options.findall(item_info_r[4*i+3])        
        item_info_dict[item_name] = Item(item_name, item_type, item_options, item_matarial)
    
    item_info.close()

    char_info = open("char_info.txt","r")
    char_info_r = char_info.readlines()

    char_info_dict = dict()

    c_name = re.compile("(?=\w)(.*?)\n")
    c_weapon = re.compile("(?=\w)(.*?)\(.*?\)")
    c_power = re.compile("(?<=\()(.*?)\)")

    for i in range(int(len(char_info_r)/2)):
        charactor_name = c_name.findall(char_info_r[2*i])[0]
        charactor_weapon = c_weapon.findall(char_info_r[2*i+1])
        charactor_power = c_power.findall(char_info_r[2*i+1])
        char_info_dict[charactor_name] = Charactor(charactor_name, charactor_weapon, charactor_power)
    
    char_info.close()

    return matarial_dict, item_info_dict, char_info_dict

##########################################################################################

def choose_item(char_name,a):

    global weapon_list, head_list, clothes_list, arm_list, leg_list

    index_weapon = char_info_dict[char_name].weapon.index(a)
    ability_setting = char_info_dict[char_name].power[index_weapon]

    weapon_list = []
    head_list = []
    clothes_list = []
    arm_list = []
    leg_list = []

    if ability_setting == "스킬증폭":
        
        for i in item_info_dict.keys():

            if item_info_dict[i].type == a and "스킬 증폭" in str(item_info_dict[i].options):
                weapon_list.append(item_info_dict[i])
            if ("스킬 증폭" or "쿨다운 감소") in str(item_info_dict[i].options):
                if not ("공격력" or "치명타 확률" or '레벨 당 공격력') in str(item_info_dict[i].options):
                    if item_info_dict[i].type == "머리":
                        head_list.append(item_info_dict[i])
                    if item_info_dict[i].type == "옷":
                        clothes_list.append(item_info_dict[i])
                    if item_info_dict[i].type == "팔":
                        arm_list.append(item_info_dict[i])
                    if item_info_dict[i].type == "다리":
                        leg_list.append(item_info_dict[i])

    elif ability_setting == "스증방어력":
        
        for i in item_info_dict.keys():
            if item_info_dict[i].type == a and "스킬 증폭" in str(item_info_dict[i].options):
                weapon_list.append(item_info_dict[i])
            if ("스킬 증폭" or "쿨다운 감소" or "방어력" or "최대 체력") in str(item_info_dict[i].options):
                if not ("공격력" or "치명타 확률" or '레벨 당 공격력') in str(item_info_dict[i].options):
                    if item_info_dict[i].type == "머리":
                        head_list.append(item_info_dict[i])
                    if item_info_dict[i].type == "옷":
                        clothes_list.append(item_info_dict[i])
                    if item_info_dict[i].type == "팔":
                        arm_list.append(item_info_dict[i])
                    if item_info_dict[i].type == "다리":
                        leg_list.append(item_info_dict[i])

    elif ability_setting == "공격력":
        
        for i in item_info_dict.keys():

            if not ("스킬 증폭" or '레벨 당 스킬 증폭') in str(item_info_dict[i].options):
                    if item_info_dict[i].type == a:
                        weapon_list.append(item_info_dict[i])
                    if item_info_dict[i].type == "머리":
                        head_list.append(item_info_dict[i])
                    if item_info_dict[i].type == "옷":
                        clothes_list.append(item_info_dict[i])
                    if item_info_dict[i].type == "팔":
                        arm_list.append(item_info_dict[i])
                    if item_info_dict[i].type == "다리":
                        leg_list.append(item_info_dict[i])

    elif ability_setting == "공격방어력":
        
        for i in item_info_dict.keys():
            if not ("스킬 증폭" or '레벨 당 스킬 증폭') in str(item_info_dict[i].options):
                if item_info_dict[i].type == a:
                    weapon_list.append(item_info_dict[i])
                if item_info_dict[i].type == "머리":
                    head_list.append(item_info_dict[i])
                if item_info_dict[i].type == "옷":
                    clothes_list.append(item_info_dict[i])
                if item_info_dict[i].type == "팔":
                    arm_list.append(item_info_dict[i])
                if item_info_dict[i].type == "다리":
                    leg_list.append(item_info_dict[i])
                    
    elif ability_setting == "치명타":

        for i in item_info_dict.keys():
            if item_info_dict[i].type == a:
                if "공격 속도" or "치명타 확률" in str(item_info_dict[i].options):
                    if not "스킬 증폭" in str(item_info_dict[i].options):
                        weapon_list.append(item_info_dict[i])
            if "공격 속도" or "치명타 확률" in str(item_info_dict[i].options):
                if not "스킬 증폭" in str(item_info_dict[i].options):
                    if item_info_dict[i].type == "머리":
                        head_list.append(item_info_dict[i])
                    if item_info_dict[i].type == "옷":
                        clothes_list.append(item_info_dict[i])
                    if item_info_dict[i].type == "팔":
                        arm_list.append(item_info_dict[i])
                    if item_info_dict[i].type == "다리":
                        leg_list.append(item_info_dict[i])

    return  weapon_list, head_list, clothes_list, arm_list, leg_list

##########################################################################################

def item_loop(weapon,limit):
    buy_item = []
    buy_num_list = []
    temp_item = []
    temp_route = []
    temp_shortest = 5

    for head in head_list:
        for clothes in clothes_list:
            for arm in arm_list:
                for leg in leg_list:
                    buy_list, buy_num, route, route_length = route_algorithm([weapon,head.name,clothes.name,arm.name,leg.name],limit)
                    
                    if route_length < temp_shortest:
                        temp_item = []
                        temp_route = []
                        buy_item = []
                        buy_num_list = []
                        buy_item.append(buy_list)
                        buy_num_list.append(buy_num)
                        temp_item.append([item_info_dict[weapon],head,clothes,arm,leg])
                        temp_route.append(route)                        
                        temp_shortest = route_length
                    elif route_length == temp_shortest:
                        buy_item.append(buy_list)
                        buy_num_list.append(buy_num)
                        temp_item.append([item_info_dict[weapon],head,clothes,arm,leg])
                        temp_route.append(route)
                    else:
                        pass

    return buy_item, buy_num_list, temp_item, temp_route

##########################################################################################

def route_algorithm(choosen,limit):

    global place_dict, route_list

    mat_list = list()
    mat_dict = dict()
    route_list = list()

    for i in choosen:
        for s in item_info_dict[i].matarial:
            mat_list.append(s)

    for i in mat_list:

        if i in mat_dict.keys():
            mat_dict[i] += 1
        else:
            mat_dict[i] = 1

    trash_list = ["가죽","나뭇가지","돌멩이","꽃"]
    for i in trash_list:
        if i in mat_dict:
            del(mat_dict[i])

    route_length = 1

    while bool(mat_dict) == True:
        place_dict = dict()
        place_algorithm(mat_dict)
        
        if sum(mat_dict.values()) <= limit:
            buy_mat_list = list()
            for i in mat_dict.keys():
                buy_mat_list.append(i)
            return buy_mat_list, len(mat_dict.values()), route_list, route_length
        
        else:
            route_length += 1

##########################################################################################

def place_algorithm(mat_dict):

    for i in mat_dict.keys():
        for s in matarial_dict[i]:
            if s in place_dict.keys():
                place_dict[s] += 1
            else:
                place_dict[s] = 1


    for i in place_dict.keys():
        if place_dict[i] == max(place_dict.values()):
            max_place = i

    route_list.append(max_place)

    del_list = []

    for i in mat_dict.keys():
        if max_place in matarial_dict[i]:
            del_list.append(i)

    for i in del_list:
        del(mat_dict[i])
    
##########################################################################################


