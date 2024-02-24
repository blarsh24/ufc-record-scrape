from googlesearch import search
import requests
from bs4 import BeautifulSoup
import time

# gets user's input on who to look up
user_raw = input("Enter a UFC fighter name: ")
user = user_raw + " tapology"

# searching google for tapology link of user's input
search_results = search(user)

# Extract the first search result URL
tapology_link = next(search_results, None)



# scrapes for fighter name on tapology using HTML
def fighter_result(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    session = requests.Session()

    try:
        response = session.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text,'html.parser')
            name = soup.select_one('div > div > div > ul > li > span')

            if name:
                value = name.get_text()
                return value
            else:
                return 'check html'
        else:
            return 'page not found, check source'
    except Exception as e:
        return f'An error occured {e}'
    finally:
        session.close()

# scarpes for fighter age using HTMl
def streak_result(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    session = requests.Session()

    try:
        response = session.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text,'html.parser')
            name = soup.select_one('div > div > div > ul > li:nth-of-type(4) > span')

            if name:
                value = name.get_text()
                return value
            else:
                return 'check html'
        else:
            return 'page not found, check source'
    except Exception as e:
        return f'An error occured {e}'
    finally:
        session.close()

# scrapes for pro MMA record from tapology using HTML
def pro_result(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    session = requests.Session()
    
    try:
        response = session.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            record = soup.find('h1', class_='prorecord')

            if record:
                value = record.get_text()
                return value
            else:
                return "check html"
        else:
            return "page not found, check source"
    except Exception as e:
        return f"An error occured:{e}"
    finally:
        session.close()

# scrapes for ufc record from tapology using HTML
def ufc_result(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    session = requests.Session()

    try:
        response = session.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            wins = soup.find('div', class_='wins')
            losses = soup.find('div', class_='losses')
            draws = soup.find('div', class_='draws')

            if wins and losses and draws: 
                w_record = wins.get_text()
                l_record = losses.get_text()
                d_record = draws.get_text()
                return w_record[1:3], l_record[1:3], d_record[1:3]
            else:
                return "check html"
        else:
            return "page not found, check source"
    except Exception as e:
        return f"An error occured:{e}"
    finally:
        session.close()

# cleans up ufc_result return for formatting
u_wins, u_losses, u_draws = map(int, ufc_result(tapology_link))

# get fighter name from tapology URL
fighter_name = fighter_result(tapology_link)
# get fighter streak from tapology URL
streak = streak_result(tapology_link)
# get pro MMA record from tapology URL
pro_record = pro_result(tapology_link)
# get ufc record from tapology URL
ufc_record = ufc_result(tapology_link)


# displays fighter stats
print('-----------------------------------')
print(f"Fighter Name:", fighter_name, "\n")
print(f"Streak:", streak)
print("Pro MMA Record:", pro_record)
print(f"UFC Record: {u_wins}-{u_losses}-{u_draws}\n")
if tapology_link:
    print("Tapology link:", tapology_link)
else:
    print("No Tapology link found for the given fighter name.")
print('-----------------------------------')
