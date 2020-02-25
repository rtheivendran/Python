
import json
from urllib.request import urlopen

response = urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json")
source = response.read()
data = json.loads(source)

print(json.dumps(data, indent=2))
#print(len(data['list']['resources']))

usd_rates = dict()

for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    #print(name, price)
    usd_rates[name] = price

print("1 US dollars = {} EUR".format( 1 * float(usd_rates['USD/EUR'])))
print("1 US dollars = {} INR".format( 1 * float(usd_rates['USD/INR'])))


