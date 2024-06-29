from api import fetch_countries_data, extract_country_info
from bd import insert_country_data, create_countries_db, create_countries_table

def main():
    create_countries_db()
    create_countries_table()

    countries_data = fetch_countries_data()
    if countries_data:
        countries_info = []
        for country in countries_data:
            country_info = extract_country_info(country)
            countries_info.append(country_info)

        insert_country_data(countries_info)
        print("Данные успешно вставлены в базу данных.")
    else:
        print("Не удалось получить данные из API.")


if __name__ == "__main__":
    main()
