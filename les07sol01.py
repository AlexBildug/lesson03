from typing import Optional

city_to_country_mapping = {
    "Belarus": ["Minsk", "Vitebsk", "Grodno"],
    "Russia": ["Moskow", "Saint-Petersburg", "Smolensk"],
    "Ukraine": ["Kiev", "Chernigov", "Sumy"]
}


def find_country(city: str) -> Optional[str]:
    """
    Check mapping and if city in cities return country
    """
    for country, cities in city_to_country_mapping.items():
        if city in cities:
            return country


def main():
    """
    Main program function to get user's input and return result
    """
    city = input("Enter city name: ")
    country = find_country(city)
    if country is not None:
        print(f"{city} is a part of {country}")
    else:
        print(f"Can't find a country for {city}")


if __name__ == "__main__":
    main()