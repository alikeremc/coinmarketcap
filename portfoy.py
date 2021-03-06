import requests
import json

api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/"
                           "latest?start=1&limit=10&convert=USD&CMC_PRO_API_KEY=f4319da6-f95c-45e8-9c73-c5232e60f0d4")

result = json.loads(api_request.content)  #çalışınca 200 çıkarsa başarılı anlamında
# print(result["status"]["total_count"])

# print(result["data"][0]["quote"]["USD"]["price"])

sepet=[
    {
    "sembol":"BTC",
    "miktar":3,
    "fiyat":48000
},
   {
    "sembol":"ADA",
    "miktar":300,
    "fiyat":1.05
},
   {
    "sembol":"LTC",
    "miktar":48,
    "fiyat":185
}
]
print("----------------")

portfoy_kar_zarar=0


for i in range(10):
    for coin in sepet:
        if result["data"][i]["symbol"] == coin["sembol"]:
            kar_zarar=result["data"][i]["quote"]["USD"]["price"]-coin["fiyat"]
            toplam_maliyet=coin["miktar"]*coin["fiyat"]
            toplam_karzarar=kar_zarar*coin["miktar"]
            portfoy_kar_zarar=portfoy_kar_zarar+toplam_karzarar

            print(result["data"][i]["symbol"] + "-" + result["data"][i]["name"])
            print("Güncel Fiyat: ${0:.2f}".format(result["data"][i]["quote"]["USD"]["price"]))
            print("Alış Fiyat: ${0:.2f}".format(coin["fiyat"]))
            print("Miktar: ${0:.2f}".format(coin["miktar"]))
            print("Kar-Zarar: ${0:.2f}".format(kar_zarar))
            print("Toplam Maliyet: ${0:.2f}".format(toplam_maliyet))
            print("Toplam Kar Zarar: ${0:.2f}".format(toplam_karzarar))
            print("-----------------")
print("*************************************")
print("Portföy Kar Zarar:",round(portfoy_kar_zarar,2))
print("*************************************")