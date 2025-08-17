import requests 

url = ""

response = requests.get(url)

with open("file.zip","wb") as f:
    f.write(response.content)