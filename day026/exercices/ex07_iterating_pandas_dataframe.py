import pandas

student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 76, 98]
}

# Looping through dictionaries
for (key, value) in student_dict.items():
    print(key and value)

student_df = pandas.DataFrame(student_dict)
print(student_df)

# Looping through data frames
for (key, value) in student_df.items():
    print(key and value)


# Loop through rows of data frame
for (index, row) in student_df.iterrows():
    print(row)
