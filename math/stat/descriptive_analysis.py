"""Module on yandex course."""

import pandas as pd

# +
path_0 = "/home/tatiana/Documents/github/Data-Science-For-Beginners"
path_1 = "/Datasets/2019.csv"
path = path_0 + path_1

df = pd.read_csv(path)
df.head()
# -

min_score = df["Score"].min()
max_score = df["Score"].max()
print(max_score)
print(min_score)

mean_score = df["Score"].mean()
print(mean_score)

median_score = df["Score"].median()
print(median_score)

# mode in all countries
print(df["Score"].mode()[0])

std_score = df["Score"].std()
print(std_score)

# sort values by the level of happiness (Score)
df_sorted = df.sort_values(by="Score", ascending=False)
df_sorted.head(10)

# +
# choose the country column
top_10_happy_countries = df_sorted["Country or region"].head(10).tolist()

print(top_10_happy_countries)
# -

# count total of all gdpes
gdp_total = df["GDP per capita"].sum()
print(gdp_total)

# count total of all gdpes in first 10 countries
gdp_10_total = df.head(10)["GDP per capita"].sum()
print(gdp_10_total)
