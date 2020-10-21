import pyshorteners
link = input("Enter URL you Wanna to shorter = ")
url = pyshorteners.Shortener()
print(url.tinyurl.short(link))