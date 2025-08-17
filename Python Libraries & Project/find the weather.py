import requests 
from bs4 import BeautifulSoup


city = input("Enter City Name :")
city_formatted = city.lower().replace("","-")




url = " "
response = requests.get(url)


soup = BeautifulSoup(response.text, ' html.parser ')


try:
    temperature = soup.fing("div",class_="h2").get_text(strip=True)
    description = soup.find("div",class_="h2").find_next("p").get_text(strip=True)

    print(f"weather in {city} :")

    print(f"weather in {temperature} :")

    print(f"weather in {description} :")

except AttributeError:
    print("Please Check the city name and try again .")

