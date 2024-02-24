import requests
from bs4 import BeautifulSoup
import time

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
                return w_record[1], l_record[1], d_record[1]
            else:
                return "check html"
        else:
            return "page not found, check source"
    except Exception as e:
        return f"An error occured:{e}"
    finally:
        session.close()

# cleans up ufc_result return for formatting
u_wins, u_losses, u_draws = map(int, ufc_result("https://www.tapology.com/fightcenter/fighters/40148-islam-makhachev"))






# get pro MMA record from tapology URL
pro_record = pro_result("https://www.tapology.com/fightcenter/fighters/40148-islam-makhachev")
# get ufc record from tapology URL
ufc_record = ufc_result("https://www.tapology.com/fightcenter/fighters/40148-islam-makhachev")


# displays MMA / UFC record
print("Pro MMA Record:", pro_record)
print(f"Pro UFC Record: {u_wins}-{u_losses}-{u_draws}")


