Cities = {
    'Toronto': {
        'Country': 'Canada',
        'Population': '2,790,000'
    },
    'Brampton': {
        'Country': 'Canada',
        'Population': '656,480'
    },
    'Plano': {
        'Country': 'The United States of America',
        'Population': '285,490'
    }
}

for city, city_info in Cities.items():
    country = city_info['Country']
    population = city_info['Population']

    print(city + " is in " + country + " and has a population of " + population)