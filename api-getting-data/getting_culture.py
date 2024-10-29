import os
import requests
import json

europeana_api_key = os.getenv('EUROPEANA_API_KEY')
data_gov_api_key = os.getenv('DATA_GOV_API_KEY')

def get_europeana_data(query):
    url = f'https://api.europeana.eu/record/v2/search.json?wskey={europeana_api_key}&query={query}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching Europeana data")
        return None

def get_gov_data(query):
    url = f'https://api.si.edu/openaccess/api/v1.0/search?q={query}&api_key={data_gov_api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching other API data")
        return None

def save_results_to_json(data, filename):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=4)

def main():
    query = 'art'  
    smithsonian_data = get_gov_data(query)
    print(smithsonian_data)
    europeana_data = get_europeana_data(query)
    print(europeana_data)
    combined_data = {
        'Europeana': europeana_data,
        'Smithsonian': smithsonian_data
    }
    save_results_to_json(combined_data, 'cultural_data.json')
    print("Data saved to cultural_data.json")

if __name__ == "__main__":
    main()