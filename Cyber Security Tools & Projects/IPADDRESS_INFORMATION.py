import os
import urllib.request as urllib2
import json


while True :
    ip = input("whats is your target ip :")
    url = "  "
    response = urllib2.urlopen(url + ip)
    data = response.read()
    values = json.loads(data)

    print("IP :"+ Values["query"])
    print("City :"+ Values["city"])
    print("ISP : "+ Values["isp"])
    print("Country :" + values["country"])
    print("Region :" + values["region"])
    print("Timezone : "+ values["timezone"])
    break


