# import csv
#
# with open("weather_data.csv") as data_file:
#     temperatures = []
#     data = csv.reader(data_file)
#     data.__next__()
#     for row in data:
#         temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict["temp"])

data_list = data["temp"].to_list()
print(data_list)

print(sum(data_list) / len(data_list))

print(data["temp"].mean())
print(data["temp"].max())

# Get data in columns
print(data.condition)
print(data["temp"])

# Get data in rows
print(data[data.day == "Monday"])

# Hottest day of the week
print(data[data.temp == data.temp.max()])

# Monday's temperature in fahrenheit
temp = int(data[data.day == "Monday"].temp)
print(f"Monday's temperature in fahrenheit: {(temp * 9 / 5) + 32}")

# Create a dataframe from scratch
data_dict_student = {
    "students": "Amy James Angela".split(" "),
    "scores": [76, 56, 65]
}
new_data = pandas.DataFrame(data_dict_student)
print(new_data)
data.to_csv("new_data.csv")
