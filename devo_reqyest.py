from inspect import signature
import time
import datetime 
import dateutil.relativedelta
import hmac
import hashlib
import json
import requests
import sys

url = "https://apiv2-us.devo.com/search/query"
#note: hard coding keys is a really bad practice and this is just poc code.
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'
query = sys.argv[1]
curr_dt = datetime.datetime.now()
now = int(round(curr_dt.timestamp()))
start_dt = (curr_dt + dateutil.relativedelta.relativedelta(days=-30))
start = int(round(start_dt.timestamp()))
payload = json.dumps({
  "query": query,
  "from": start,
  "to": now,
  "limit": 10,
  "mode": {
    "type": "json/compact"
  }
})
a = bytes(api_secret, 'utf-8')
timestamp = str(int(time.time()) * 1000)
data = payload
message = api_key + data + timestamp
b = bytes(message, 'utf-8')
sign = hmac.new(a, b, digestmod=hashlib.sha256).hexdigest()
headers = {
  'Content-Type': 'application/json',
  'x-logtrust-apikey': api_key,
  'x-logtrust-sign': sign,
  'x-logtrust-timestamp': timestamp
}
response = requests.request("POST", url, data=payload, headers=headers)
#print(response.text)
#print(response.json())
json_object = json.dumps(response.json(), indent = 4)
with open('response.txt', 'a') as outfile:
    outfile.write("\n"+ "Query results from the last 30 Days for query " + query + json_object +"\n")
