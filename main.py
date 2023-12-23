import json
import requests
import smtplib
from bs4 import BeautifulSoup
from email.message import EmailMessage
from datetime import datetime

log = ""

def check_availability(url):
    global log
    try:
        page = requests.urlopen(url)
        soup = BeautifulSoup(page, features='html.parser')

        if phrase in soup.text:
            return False
        return True
    except:
        log += "Error parsing the website"


def main():
    url = "https://www.bestbuy.ca/en-ca/product/playstation-5-slim-console-marvel-s-spider-man-2-bundle/17390652"
    phrase = "PlayStation 5"
    available = check_availability(url, phrase)

    if available:

        with open('config.json') as file:
            config = json.load(file)
            username = config['username']
            password = config['password']
            fromAddress = config['fromAddress']
            toAddress = config['toAddress']

        msg = EmailMessage()
        msg['Subject'] = "Playstation 5 is in stock!"
        msg['From'] = config['fromAddress']
        msg['To'] = config['toAddress']
        msg.set_content("It seems that there is a PS5 available at " + url)

        server = smtplub.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.Login(username,password)

        server.send_message(msg)
        server.quit()

        

if __name__ == '__main__':
    main()
