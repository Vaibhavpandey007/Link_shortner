import pyshorteners

link = input("Enter the link: ")

shortener = pyshorteners.Shortener()
shortened_link = shortener.tinyurl.short(link)
print("Shortned Link: ",shortened_link)