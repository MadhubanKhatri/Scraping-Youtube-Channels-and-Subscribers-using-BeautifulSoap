import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.statsheep.com/p/Top-Subscribers"
r = requests.get(url)
data = r.content
soap = BeautifulSoup(data,'html.parser')
td = soap.find_all("td",class_="data")
anchors = soap.find_all('a')[28:]

channel_name = []
subscribers = []

for i in td:
    subscribers.append(i.text.strip())
for i in anchors:
    if i.text == "2":
        break
    channel_name.append(i.text)

dict = {
    "Name": channel_name,
    "Subscribers": subscribers
}

df = pd.DataFrame(dict)
df.to_csv("youtube_data.csv",index=False)

