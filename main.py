import requests
import hashlib
import timeit
import pandas as pd
import db


def encode_lang(data):
    return hashlib.sha1(data.encode('utf-8')).hexdigest()

def make_row(country):
    new_row = {
        'region': country.get('region'),
        'country_name': country.get('name'),
        'language': encode_lang(str([language.get('name') for language in country.get('languages')]))
    }
    return new_row

def main():
    url = 'https://restcountries.com/v2/all'
    response = requests.get(url)
    country_list = response.json()
    country_data = []
    print(country_list[0])
    for country in country_list:
        new_country = make_row(country)
        new_country['time_ms'] = timeit.timeit(f"make_row({country})", globals=globals(), number=1) * 1000
        country_data.append(new_country)
    df = pd.DataFrame(country_data)
    average = df['time_ms'].describe()['mean']
    max_value = df['time_ms'].describe()['max']
    min_value = df['time_ms'].describe()['min']
    total = df['time_ms'].sum()
    print('Tiempo (ms) Promedio:', average)
    print('Tiempo (ms) Maximo:', max_value)
    print('Tiempo (ms) Minimo:', min_value)
    print('Tiempo (ms) Total:', total)
    df.to_sql('country', db.con, if_exists='append')


def export_data():
    df = pd.read_sql('select * from country', db.con)
    df.to_json(r'./data.json')
    db.con.close()


if __name__ == '__main__':
    main()
    export_data()