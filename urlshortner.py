import pyshorteners
import pyshorteners.shorteners

url = input("Enter the url: \n")

print("URL aftre shortening: ",pyshorteners.shorteners().tinyurl(url))
