import requests
from flask import Flask, jsonify, request
import json
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


countries = json.load(open("countries.json"))

def get_data(country, state, date, month, year):
    if country.title() not in countries or state not in countries[country.title()]:
        return {
            "error": "Country/state not found"
        }
    data = requests.get(f"https://phasesmoon.com/{country}/{state}/moonday{date}{month}{year}.html").text
    with open("temp.html", "w", encoding="utf-8") as f:
        f.write(data)
    soup = BeautifulSoup(data, 'html.parser')

    moon_phase = soup.select_one("body > div.container > div.row.headerdetails > div:nth-child(1) > ul > li.phasename > strong").string
    moon_rise = soup.select_one("body > div.container > div.row.headerdetails > div:nth-child(1) > ul > li:nth-child(2)").string.replace("Moonrise today: ", "")
    moon_set = soup.select_one("body > div.container > div.row.headerdetails > div:nth-child(1) > ul > li:nth-child(3)").string.replace("Moon set today: ", "")
    moon_duration = soup.select_one("body > div.container > div.row.headerdetails > div:nth-child(1) > ul > li:nth-child(4)").string.replace("Duration:", "")
    moon_visibility = soup.select_one("body > div.container > div.row.headerdetails > div:nth-child(3) > div.phasename").string.replace("% Visible", "")
    moon_constellation = soup.select_one("body > div.container > div.row.headerdetails > div:nth-child(3) > div:nth-child(3)").string.replace("Moon's constellation ", "").replace("\n", "")
    moon_horoscope = soup.select_one("body > div.container > div.row.headerdetails > div:nth-child(3) > div:nth-child(4)").string.replace("Horoscope is ", "").replace("\n", "")
    moon_age = soup.select_one("body > div.container > div:nth-child(4) > table > tbody > tr:nth-child(5) > td:nth-child(2)").string
    moon_angle = soup.select_one("body > div.container > div:nth-child(4) > table > tbody > tr:nth-child(6) > td:nth-child(2)").string
    moon_distance = soup.select_one("body > div.container > div:nth-child(4) > table > tbody > tr:nth-child(7) > td:nth-child(2)").string
    moon_img = soup.select_one("body > div.container > div.row.headerdetails > div.col4.text-center > div > img")["src"]

    return {
        "phase": moon_phase,
        "rise": moon_rise,
        "set": moon_set,
        "duration": timedelta(hours=int(moon_duration.split(" ")[0]), minutes=int(moon_duration.split(" ")[3])).total_seconds(),
        "visibility": float(moon_visibility),
        "constellation": moon_constellation,
        "horoscope": moon_horoscope,
        "age": moon_age,
        "angle": moon_angle,
        "distance": moon_distance,
        "img": moon_img
    }

# print(get_data("india", "new-delhi", "22", "october", "2023"))
