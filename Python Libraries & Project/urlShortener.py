import pyshorteners

long_urls = input("enter the url to shorten")

type_tiny = pyshorteners.shortener()
short_url = type_tiny.tinyurl.short(long_urls)

print("the shortened URL IS :" + short_url)