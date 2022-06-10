import requests
from bs4 import BeautifulSoup as bs
user_name = "AndreaMMK" #input("enter")
url = "https://github.com/"+user_name#Enter site url
results=requests.get(url)

soup =bs(results.content,"html.parser")
profile_pic = soup.find('img',{'alt':'Avatar'})
print(profile_pic)
