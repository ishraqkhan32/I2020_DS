import csv
import requests
from bs4 import BeautifulSoup as bs

url = 'https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data'

# helper function to return appropriately formatted cell value
def convert_cell(cell):
    try:
        return int(cell.text.strip().replace(',',''))
    except:
        return None

# returns rate rounded to 3 decimals places if non-NA inputs
def calculate_rate(part, whole):
    try:
        return round(part/whole, 3)
    except TypeError:
        return None

if __name__ == '__main__':

    # get soup from url
    r = requests.get(url)
    soup = bs(r.text, features="html.parser")

    # get covid table 
    table = soup.find('table', id='thetable')

    # parse table for body and row elements
    tbody = table.find('tbody')
    rows = tbody('tr') # list of all table rows
    sub_rows = rows[2:-2] # remove table headers and non-data rows

    all_data = []

    for row in sub_rows:
        # get country name
        country = row('th', scope='row')[1].find('a').text

        # access data for country from row
        row_data = row('td')[:3]
        cases = convert_cell(row_data[0])
        deaths = convert_cell(row_data[1])
        recoveries = convert_cell(row_data[2])

        # calculate death and recovery rate
        death_rate = calculate_rate(deaths,cases)
        recovery_rate = calculate_rate(recoveries,cases)

        # store data in global list
        row_data = [country, cases, deaths, recoveries, death_rate, recovery_rate]
        all_data.append(row_data)

    # create output csv
    with open('ishraqkhan-covid-report.csv', 'w', newline='') as f:
        # create writer object
        writer = csv.writer(f)

        # add headers
        header = ['country', 'cases', 'deaths', 'recoveries', 'death_rate', 'recovery_rate']
        writer.writerow(header)

        # add table data
        for data in all_data:
            writer.writerow(data)