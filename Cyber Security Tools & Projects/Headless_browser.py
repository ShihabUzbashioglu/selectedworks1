from selenium import webdriver

from selenium.webdriver.chrome.options import Options

#config

Options = Options()
Options.add_argument("--headless")         #without window
options.add_argument("--disable-gpu")       #like upthere but optional
Options.add_argument("--window-size=1920x1080")     


# loading browser
driver = webdriver.chrome(Options=Options)

#open webpage

link = "www.example.com"
driver.get(link)


# page title

print("page title  :",driver.title)


#close browser
driver.quit()