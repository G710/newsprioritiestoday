import os
import csv

from datetime import datetime
from requests_html import HTMLSession

sources = []

with open("sources.csv", "r") as file:
    reader = csv.reader(file, delimiter=",")
    header = next(reader)

    for row in reader:
        entry = {}
        for index, item in enumerate(header):
            entry[item] = row[index]
        sources.append(entry)

def fetch_news(source):
    print(source)
    print("Fetching news from " + source["name"])
    session = HTMLSession()
    r = session.get(source["url"])

    target_directory = "../newsprioritiestoday-data/raw/" + source["directory"]
    if not os.path.exists(target_directory):
        print("Path for " + source["name"] + "does not exist. Creating path.")
        os.makedirs(target_directory)
    with open(target_directory + "/" + source["directory"] + "_" + str(datetime.now()) + ".txt", "w") as file:
        print("Saving news from " + source["name"])
        file.write(r.html.raw_html.decode())

for source in sources:
    fetch_news(source)