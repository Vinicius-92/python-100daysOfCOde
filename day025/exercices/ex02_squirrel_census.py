import pandas

data = pandas.read_csv("squirrel_census.csv")

# My first approach
fur = data["Primary Fur Color"]
fur.value_counts().to_frame().to_csv("counting_fur_color.csv")

# Course approach
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": "Gray Cinnamon Black".split(" "),
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
print(df)
