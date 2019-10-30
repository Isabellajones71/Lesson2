#for loop structure
# A for loop is used for iterating over a
# sequence (that is either a list, a tuple,
# a dictionary, a set, or a string).
# list_data = [1, 2, 3, 4, 5]
# for num in list_data:
#     print(num * 2)
# embedded_lists = [[1,2,3],[4,5,6]]
# for data in embedded_lists:
#     print(data)
#Loops for dictionaries
# dict_data = {1: {"name": "Bronson", "money": "$0.05"},
#              2: {"name": "Masha", "money": "$3.66"},
#              3: {"name": "Roscoe", "money": "$1.14"}}
# #Fetching key values
# for k in dict_data:
#     print(k)
# #Fetching vaues from the dictionary
# for item in dict_data.values():
#     print(item)
#
# for items in dict_data.values():
#     print(items['name'])

list_data = [1, 2, 3, 4, 5]

for num in list_data:
    if num == 3:
        print('I found three')
    elif num > 3:
        print('gone too far')
    else:
        print("too soon")
