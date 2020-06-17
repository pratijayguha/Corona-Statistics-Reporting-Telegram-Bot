from bs4 import BeautifulSoup
import requests
import json

URL = 'https://api.covid19api.com/summary'

class country_details():
    def __init__(self,new_cases,tot_cases,new_rec):
        self.new_cases = new_cases
        self.tot_cases = tot_cases
        self.new_rec = new_rec
        self.message = message = "***INDIA***"+\
                                "\nTotal cases till date: "+str(self.tot_cases)\
                                +"\nNew cases yesterday: "+str(self.new_cases)+\
                                "\nNew recoveries yesterday: "+str(self.new_rec)

class corona_fetch():

    def get_corona_tally(self):
        result = requests.get(URL)
        soup = BeautifulSoup(result.content, 'html.parser')
        # text = str(soup.title)
        data = json.loads(str(soup))

        for country in data["Countries"]:
            if country["Country"]=='India':
                india = country_details(new_cases=country["NewConfirmed"],
                                        tot_cases=country["TotalConfirmed"],
                                        new_rec=country["NewRecovered"]
                                        )

        return india.message
