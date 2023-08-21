import requests
from bs4 import BeautifulSoup

main_url = "enter url"
req_url = requests.get(main_url)

soup = BeautifulSoup(req_url.content, "html.parser")

p1 = soup.find("p")
p2 = soup.find_all("p")[1]
#prints the first and second paragraph
print(" ")
print(p1.get_text())
print(" ")
print(p2.get_text())
print(" ")
