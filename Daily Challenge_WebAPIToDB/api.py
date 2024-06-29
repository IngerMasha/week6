import requests

def fetch_countries_data():
    url = 'https://restcountries.com/v3.1/all'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Не удалось получить данные: {response.status_code}")
        return None

def extract_country_info(country):
    name = country.get('name', {}).get('common', '')
    capital = country.get('capital', '')
    subregion = country.get('subregion', '')
    population = country.get('population', 0)
    # flag = country.get('flags', [''])[0]
    return {
        'name': name,
        'capital': capital,
        'subregion': subregion,
        'population': population
        # 'flag': flag
    }
