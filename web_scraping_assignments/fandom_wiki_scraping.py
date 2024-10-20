import requests
from bs4 import BeautifulSoup
import json

# URL of the Wikipedia page
url = "https://ja.wikipedia.org/wiki/新原勇"

# Send a GET request to fetch the page content
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Extract the title (Name)
title = soup.find("h1", {"id": "firstHeading"}).text

# Extract the introductory paragraph
intro_paragraph = soup.find("p").text

# Extract birth and other personal details from the infobox
infobox = soup.find("table", {"class": "infobox"})
occupation = None

if infobox:
    rows = infobox.find_all("tr")
    for row in rows:
        header = row.find("th")
        data = row.find("td")
        if header and data:
            if "職業" in header.text: 
                occupation = data.text.strip()

# Prepare the data to save into a JSON file
result_data = {
    "name": title,
    "introduction": intro_paragraph.strip(),
    "occupation": occupation if occupation else "Not found",
}

# Save the result to a JSON file
with open('result.json', 'w', encoding='utf-8') as json_file:
    json.dump(result_data, json_file, ensure_ascii=False, indent=4)

print("Data saved to result.json")

