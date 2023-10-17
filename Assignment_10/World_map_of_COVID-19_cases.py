import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load the world map shapefile
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Load the COVID-19 data from the provided URL
covid19_data_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
covid19_data = pd.read_csv(covid19_data_url)

country_column_name = 'Country/Region'

# Group the COVID-19 data by country and sum cases across all dates
covid19_data_grouped = covid19_data.groupby(country_column_name).sum().reset_index()

# Merge the world map data with the COVID-19 data based on the "Country" column
merged_data = world.merge(covid19_data_grouped, left_on="name", right_on=country_column_name, how="left")



#plot a chloropleth map with COVID-19 cases:

t='1/10/23'

fig, ax = plt.subplots(1, 1, figsize=(15, 10))

world.boundary.plot(ax=ax, linewidth=1, color='k')  # Add country borders
merged_data.plot(column=t, cmap='YlOrRd', legend=True, ax=ax)
ax.set_title(f'COVID-19 Cases Worldwide ({t})')

plt.show()

plt.savefig('covid19_world_map.png')