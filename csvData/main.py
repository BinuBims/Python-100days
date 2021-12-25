# # with open("weather_data.csv") as weather:
# #     print(weather.readlines())

# # import csv

# # with open("weather_data.csv") as weather:
# #     data = csv.reader(weather)
# #     temperature =  []
# #     for row in data:
# #         try:
# #             temperature.append(int(row[1]))
# #         except:
# #             continue
# #     print(temperature)

import pandas as pd

# data = pd.read_csv("weather_data.csv")
# temp_list = max(data["temp"])
# print(temp_list)

squarel_df = pd.read_csv("squarel.csv")
#fur_color = squarel_df["Primary Fur Color"]
print(squarel_df.groupby("Primary Fur Color").sum())
