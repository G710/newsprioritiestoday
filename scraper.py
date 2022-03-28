import os
import csv

from datetime import datetime
from requests_html import HTMLSession


def get_sources():
    sources = []
    with open("../newsprioritiestoday-data/sources.csv", "r") as file:
        reader = csv.reader(file, delimiter=",")
        header = next(reader)

        for row in reader:
            entry = {}
            for index, item in enumerate(header):
                entry[item] = row[index]
            sources.append(entry)
    
    return sources

def fetch_news(source):
    print("Fetching news from " + source["name"])
    session = HTMLSession()
    r = session.get(source["url"])

    target_directory = "../newsprioritiestoday-data/raw/" + source["directory"]
    if not os.path.exists(target_directory):
        print("Path for " + source["name"] + "does not exist. Creating path.")
        os.makedirs(target_directory)
    with open(target_directory + "/" + source["directory"] + "_" + str(datetime.now().strftime("%Y-%m-%d %H")) + "h.html", "w") as file:
        file.write(r.html.raw_html.decode())

sources = get_sources()
for source in sources:
    fetch_news(source)