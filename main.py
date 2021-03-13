import requests
import json

api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/"
                           "latest?start=1&limit=10&convert=USD&CMC_PRO_API_KEY=**********************************")

result = json.loads(api_request.content)  #çalışınca 200 çıkarsa başarılı anlamında
# print(result["status"]["total_count"])

# print(result["data"][0]["quote"]["USD"]["price"])

sepet=["BTC","LTC","ADA"]

print("----------------")

for i in range(10):
    for coin in sepet:
        if result["data"][i]["symbol"] == coin:

            print(result["data"][i]["symbol"] + "-" + result["data"][i]["name"])

            print("Price: ${0:.2f}".format(result["data"][i]["quote"]["USD"]["price"]))

            print("-----------------")
