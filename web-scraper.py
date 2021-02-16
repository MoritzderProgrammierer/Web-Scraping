from bs4 import BeautifulSoup
import requests
import csv

URL = "https://www.realtotal.de/real-absage-nagelsmann-waere-in-zukunft-vielleicht-anders/"
source = requests.get(URL).text


soup = BeautifulSoup(source, "lxml")

csv_file = open('web_scrape.csv', 'w', newline = '')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'author', 'date', "amount_comments"])

meta = soup.find("div", class_="post-meta")
headline = soup.find("h1", class_="post-title").text
date = meta.time["datetime"]
author = meta.span.text.replace(" von ", "")
amount_comments = int(meta.find("span", class_="post-comments").text.replace("Kommentar", "").replace("e", "").replace(" ", ""))

csv_writer.writerow([headline, date, author, amount_comments])

