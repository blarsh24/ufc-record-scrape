from googlesearch import search
import requests
from bs4 import BeautifulSoup
import time

# gets user's input on who to look up
user_raw = input("Enter a UFC fighter name: ")
ufc_stats = user_raw + " ufcstats"

# searching google for ufc stats link of user's input
ufc_stats_results = search(ufc_stats)

# Extract the first search result URL
ufc_stats_link = next(ufc_stats_results, None)


# scrapes for fighter name on ufc stats using HTML
def fighter_result(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    session = requests.Session()

    try:
        response = session.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text,'html.parser')
            name = soup.find('span', class_="b-content__title-highlight")

            if name:
                value = name.get_text()
                return value.strip()
            else:
                return 'check html'
        else:
            return 'page not found, check source'
    except Exception as e:
        return f'An error occured {e}'
    finally:
        session.close()





def last_five(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    session = requests.Session()

    try:
        response = session.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text,'html.parser')
            fight_table = soup.find('table')

            if fight_table:
                print(fight_table)
                pass #for fight in fight_table:
                    #print(fight)
            else:
                return 'check html'
        else:
            return 'page not found, check source'
    except Exception as e:
        return f'An error occured {e}'
    finally:
        session.close()
    

last_five(ufc_stats_link)