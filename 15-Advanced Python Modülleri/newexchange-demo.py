import requests
import json

api_url = "https://api.exchangerate.host/latest?base="
api_url2= "&source=ecb"

bozdurulan_doviz = input("bozdurulan döviz türü: ")
alinan_doviz     = input("alınan döviz türü: ")
miktar = int(input(f"Ne kadar {bozdurulan_doviz} bozdurmak istiyorsunuz: "))


result = requests.get(api_url+bozdurulan_doviz+api_url2)
result = json.loads(result.text)


print("1 {0} = {1} {2} ".format(bozdurulan_doviz, result["rates"][alinan_doviz], alinan_doviz) )
print("{0} {1} = {2} {3} ".format(miktar, bozdurulan_doviz, miktar*result["rates"][alinan_doviz],alinan_doviz ))