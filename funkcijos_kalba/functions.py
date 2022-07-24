# dude explains using functions from different file perfectly
# https://www.youtube.com/watch?v=jx4eysaLTrg&ab_channel=CodeFather


def filter_countries(original_countries, country_filter):
    filtered_countries = []

    for country in original_countries:
        if country.startswith(country_filter):
            filtered_countries.append(country)

    return filtered_countries


def get_first_country(original_countries):
    return original_countries[0]
