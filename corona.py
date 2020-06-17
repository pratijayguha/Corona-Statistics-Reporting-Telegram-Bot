from bs4 import BeautifulSoup
import requests

URL = 'https://www.mygov.in/covid-19'

class corona_fetch():

    def get_corona_tally(self):
        result = requests.get(URL)
        soup = BeautifulSoup(result.content, 'html.parser')
        # text = str(soup.title)
        num = soup.body.find_all('span', {"class": "icount"})
        act_cases = int(num[0].contents[0])
        rec_cases = int(num[1].contents[0])
        dec_cases = int(num[2].contents[0])
        mig_cases = int(num[3].contents[0])
        tot_cases = act_cases+rec_cases+dec_cases+mig_cases
        message = "***INDIA***\nTotal cases till date: "+str(tot_cases)+"\nActive cases: "+str(act_cases)+"\nRecovered cases: "+str(rec_cases)+"\nDeceased cases: "+str(dec_cases)+"\nMigrated cases: "+str(mig_cases)
        return message

