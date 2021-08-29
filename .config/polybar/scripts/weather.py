#!/bin/python
# -*- coding: utf-8 -*-

# Surf to https://openweathermap.org/city

import requests

CITY = "5959326"
API_KEY = "b2015fcc1a3cee3f5834249d4d1a0416"
UNITS = "Imperial"
UNIT_KEY = "F"
LANG = "en"

REQ = requests.get("http://api.openweathermap.org/data/2.5/weather?id={}&lang={}&appid={}&units={}".format(CITY, LANG,  API_KEY, UNITS))
try:
    # HTTP CODE = OK
    if REQ.status_code == 200:
        CURRENT = REQ.json()["weather"][0]["description"].capitalize()
        TEMP = int(float(REQ.json()["main"]["temp"]))
        print("{}, {} °{}".format(CURRENT, TEMP, UNIT_KEY))
    else:
        print("Error: BAD HTTP STATUS CODE " + str(REQ.status_code))
except (ValueError, IOError):
    print("Error: Unable print the data")
