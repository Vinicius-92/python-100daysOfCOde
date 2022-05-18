# with open("file1.txt") as file:
#     file1 = file.read().split()
#     list1 = [int(n) for n in file1]

# with open("file2.txt") as file:
#     file2 = file.read().split()
#     list2 = [int(n) for n in file2]

with open("file1.txt") as file1, open("file2.txt") as file2:
    list_file_1 = [n for n in file1.read().split()]
    result = [int(n) for n in file2.read().split() if n in list_file_1]

# result = [n for n in list1 if n in list2]
print(result)
