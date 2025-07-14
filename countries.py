import pandas as pd

countries = pd.read_csv("countries.csv")

unique_countries = pd.read_csv("countries_unique.csv")

print(unique_countries["Country"].head(40))

print(countries["Name"].head(40))

list_1 = unique_countries["Country"]

list_2 = countries["Name"]

print(bool(set(list_1).intersection(list_2)))