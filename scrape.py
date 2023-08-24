import requests
from bs4 import BeautifulSoup

countries_ = {}

for _ in ["", "2"]:
    data = requests.get(f"https://phasesmoon.com/countries{_}/").text
    soup = BeautifulSoup(data, 'html.parser')
    countries = soup.select("body > div.container > div.cols > div")
    for i in countries:
        # print(i.img)
        states_ = []
        last = -1
        n=1
        while last !=0:
            last=0
            data2 = requests.get(i.a['href']).text if n == 1 else requests.get(i.a['href'][:-1]+str(n)).text
            soup2 = BeautifulSoup(data2, 'html.parser')
            states = soup2.select("body > div.container > div.cols > div")
            for j in states:
                if j.img == None:
                    last+=1
                states_.append(j.div.a["href"].replace("https://phasesmoon.com/", "").split("/")[1])
            n+=1
        countries_[i.a.string] = states_
        print(f"{i.a.string}: {len(states_)} states")

import json

json.dump(countries_, open("countries.json", "w", encoding="utf-8"))