from typing import Tuple


strInput = input("Input comma seperated list: ")

items = strInput.split(',')

list = []

for item in items:
    list.append(item.strip())

tup = tuple(list)
print("List",list)
print("Tuple",tup)