import requests
from bs4 import BeautifulSoup
from csv import writer

location = "C:\\Users\\Chris\\Desktop\\result.csv" #Change as required, unless your windows user dir name is also Chris

# Creates a request from the hipster SF bootcamp's front page URL
req = requests.get("https://www.rithmschool.com/blog")

# Send the req to BS4 for parsing
soup = BeautifulSoup(req.text, "html.parser")

# Finds all article tags for scraping
articles = soup.find_all("article")
#print(articles)

with open(location, "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link", "date"])
    
    # Scrape all a tags, blog titles, URLs, and corresponding article dates.
    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        url = a_tag["href"]
        date = article.find("time")["datetime"]
        #print(title,url,date)
        csv_writer.writerow([title,url,date])
