from bs4 import BeautifulSoup
import requests
import json
from flask import Flask
from flask_cors import CORS, cross_origin
import numpy
import time


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
    # print(clean_data)
    return clean_data

def get_item(name):
    get_index_item = clean_data["name_item"].index(name)
    data_list = []
    data_list.append(clean_data["id_item"][get_index_item])
    data_list.append(clean_data["name_item"][get_index_item])
    data_list.append(clean_data["sell_offers_item"][get_index_item])
    data_list.append(clean_data["buy_orders_item"][get_index_item])
    data_list.append(clean_data["format_sellPrice_item"][get_index_item])
    data_list.append(clean_data["format_BuyPrice_item"][get_index_item])
    print(data_list)


i = 1
while i != 5: # Boucle Infini
    get_all_item("https://crossoutdb.com/data/search?l=undefined&_=1614526857308")
    time.sleep(60.0)

# Pour mieux comprendre ne pas hésitez à regarder la magnifique vidéo de NinjaScripter au niveau réseaux: https://www.youtube.com/watch?v=pQL-Bflq_pw


# app = Flask(__name__)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
# 
# @app.route('/get_otacos')
# @cross_origin()
# def main():
#     return otacos_infos
# 
# @app.route('/get_otacos/boissons')
# @cross_origin()
# def main_boissons():
#     return {"boissons" : otacos_infos["boissons"]}
# 
# if __name__ == "__main__":
#     app.run(debug=True)
