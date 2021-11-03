import requests
from twilio.rest import Client
coinMarketCap_Key=""#API KEY
watchList=["BTC","ETH","DOGE"]
targets=[45000.0,2500.0,0.23]
account_sid = ""#Twilio account sid
auth_token  = ""#Twilio authtoken
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
client = Client(account_sid, auth_token)
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
head = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': "",#CMC API KEY
}
data=requests.get(url,params=parameters,headers=head).json()
currencies=data['data']
symbol=[]
price=[]
for i in currencies:
    if(i['symbol'] in watchList):
        symbol.append(i['symbol'])
        price.append(i['quote']['USD']['price'])
msg=""
for x in range(len(price)):
    if(price[x]<=targets[x]):
      msg+=watchList[x]+" "+"$"+str(price[x]+"\n")
if(len(msg)>0):
  message = client.messages.create(
  body=watchList[x]+" is at "+str(price[x]),
  from_="",#Twilio number
  to="" #delivery number
  )
