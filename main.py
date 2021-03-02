from bs4 import BeautifulSoup
import requests
import json

clean_data = {}
clean_data["id_item"] = []
clean_data["name_item"] = []
clean_data["sell_offers_item"] = []
clean_data["buy_orders_item"] = []
clean_data["format_sellPrice_item"] = []
clean_data["format_BuyPrice_item"] = []

def get_all_item(url):
    response = requests.get(url)
    json_item = json.loads(response.text)
    clean_json = json_item["data"] # [934]
    
    for item in range(len(clean_json)):
        clean_data["id_item"].append(clean_json[item]["id"])
        clean_data["name_item"].append(clean_json[item]["name"])
        clean_data["sell_offers_item"].append(clean_json[item]["sellOffers"])
        clean_data["buy_orders_item"].append(clean_json[item]["buyOrders"])
        clean_data["format_sellPrice_item"].append(clean_json[item]["formatSellPrice"])
        clean_data["format_BuyPrice_item"].append(clean_json[item]["formatBuyPrice"])
    # print(clean_json[0]["name"])
    # print(clean_data["sell_offers_item"])
    return clean_data
    
def get_item(name, id_, name_, sellOffers, buyOrders, sellPrice, buyPrice):
    get_index_item = clean_data["name_item"].index(name)
    # print(name_item)
    data_list = []
    if id_ == True:
        data_list.append(clean_data["id_item"][get_index_item])
    elif name_ == True:
        data_list.append(clean_data["name_item"][get_index_item])
    elif sellOffers == True:
        data_list.append(clean_data["sell_offers_item"][get_index_item])
    elif buyOrders == True:
        data_list.append(clean_data["buy_orders_item"][get_index_item])
    elif sellPrice == True:
        data_list.append(clean_data["format_sellPrice_item"][get_index_item])
    elif buyPrice == True:
        data_list.append(clean_data["format_BuyPrice_item"][get_index_item])
    else:
        print("ERR: Veuillez entrer des paramètres valide (True ou False)")

get_item("RN Seal", True, False, True, True, False, True) # Mardi, tester cette fonction 
get_all_item("https://crossoutdb.com/data/search?l=undefined&_=1614526857308")
breakpoint()
# Pour mieux comprendre ne pas hésitez à regarder la magnifique vidéo de NinjaScripter au niveau réseaux: https://www.youtube.com/watch?v=pQL-Bflq_pw