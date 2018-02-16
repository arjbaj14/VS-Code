import csv
import requests
from BeautifulSoup import BeautifulSoup
import sys
import httplib
import socket
import json

url = 'http://www.showmeboone.com/sheriff/JailResidents/jailResident.asp'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('tbody', attrs={'class': 'stripe'})

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("./inmate.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(
    ["Last", "First", "Middle", "Gender", "Race", "Age", "City", "State"])
writer.writerows(list_of_rows)
