countries = input().split(", ")
capitals = input().split(", ")

# country_capitols = dict(zip(countries, capitals))
country_capitols = {country: capital for country, capital in zip(countries, capitals)}

for country, capital in country_capitols.items():
    print(f"{country} -> {capital}")