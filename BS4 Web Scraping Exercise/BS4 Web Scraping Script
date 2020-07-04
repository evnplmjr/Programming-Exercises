from bs4 import BeautifulSoup
import requests
import csv

url = "https://blog.treasuredata.com/blog/2016/03/15/self-study-list-for-data-engineers-and-aspiring-data-architects/"
response = requests.get(url)
source = response.text
soup = BeautifulSoup(source, "lxml")

csv_file = open("data_engg_study_list.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Title", "Link"])

for notes in soup.find_all("p"):
    titles = notes.find("b", text=True)
    print(titles)

    for link in notes.find_all("a"):
        links = link.get("href")
        print(links)
        
    csv_writer.writerow([titles, links])

csv_file.close()
