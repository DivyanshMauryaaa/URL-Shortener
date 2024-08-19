import pyshorteners

shortner = pyshorteners.Shortener()
url = input("URl: ")

short_url = shortner.tinyurl.short(url)
 
print("The Shortened URL is: " + short_url)