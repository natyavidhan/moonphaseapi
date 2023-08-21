import requests
from flask import Flask, jsonify, request
import json
from bs4 import BeautifulSoup

data = requests.get("https://phasesmoon.com/india/new-delhi/moonday22October2023.html").text
soup = BeautifulSoup(data, 'html.parser')

# Find the div with class "row headerdetails"
headerdetails_div = soup.find('div', class_='row headerdetails')

# Extracting moon phase details
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


print("Moon Phase:", moon_phase)
print("Moonrise:", moon_rise)
print("Moonset:", moon_set)
print("Moon Duration:", moon_duration)
print("Moon Visibility:", moon_visibility)
print("Moon Constellation:", moon_constellation)
print("Moon Horoscope:", moon_horoscope)
print("Moon Age:", moon_age)
print("Moon Angle:", moon_angle)
print("Moon Distance:", moon_distance)