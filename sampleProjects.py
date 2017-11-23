from urllib2 import Request, urlopen, URLError
from dateutil.parser import parse
import json
import datetime


# Bitcoin rate
print "Bitcoin rate"
request = Request('https://api.coindesk.com/v1/bpi/currentprice.json')

currentPrice = urlopen(request).read()
rate = json.loads(currentPrice)
print "Updated in {}".format(parse(rate['time']['updated']).strftime('%d/%m/%Y'))
print "USD rate is ", rate['bpi']['USD']['rate']
print "GBP rate is ", rate['bpi']['GBP']['rate']
print "EUR rate is ", rate['bpi']['EUR']['rate']

# Litecoin rate
print "Litecoin rate"
request = Request('https://api.coinmarketcap.com/v1/ticker/litecoin/')

response = urlopen(request)
currentPrice = response.read()
rate = json.loads(currentPrice)

print "Updated in ", datetime.datetime.now().strftime('%d/%m/%Y')
print "USD rate is ", rate[0]['price_usd']
