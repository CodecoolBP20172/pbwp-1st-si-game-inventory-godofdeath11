# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification
from collections import Counter
import itertools
import csv


# Displays the inventory.


def display_inventory(inventory):
    print("Inventory: ")
    for value, key in inventory.items():
        print (value, key)


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    inventory = Counter(inventory)
    inventory.update(added_items)
    return inventory

# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order


def print_table(inventory, order=None):
    if order == "count,desc":
        print("Inventory: ")
        print (str("count").rjust(7, " "), str("itemname").rjust(13, " "))
        print('-' * 21)
        inv_sorted_keys = sorted(inventory, key=inventory.get, reverse=True)
        for r in inv_sorted_keys:
            print (str(inventory[r]).rjust(7, " "), r.rjust(13, " "))
        print('-' * 21)
        print("Total number of items: " + str(sum(inventory.values())))
    elif order == "count,asc":
        print("Inventory: ")
        print (str("count").rjust(7, " "), str("itemname").rjust(13, " "))
        print('-' * 21)
        inv_sorted_keys2 = sorted(inventory, key=inventory.get, reverse=False)
        for r in inv_sorted_keys2:
            print (str(inventory[r]).rjust(7, " "), r.rjust(13, " "))
        print('-' * 21)
        print("Total number of items: " + str(sum(inventory.values())))
    elif order is None:
        print("Inventory: ")
        print (str("count").rjust(7, " "), str("itemname").rjust(13, " "))
        print('-' * 21)
        for values, keys in inventory.items():
            print(str(keys).rjust(7, " "), values.rjust(13, " "))
        print('-' * 21)
        print("Total number of items: " + str(sum(inventory.values())))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    f = open(filename)
    csv_f = csv.reader(f)
    new_list = list(csv_f)
    merged = list(itertools.chain.from_iterable(new_list))
    inventory = Counter(inventory)
    inventory.update(merged)
    return inventory

# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).


def export_inventory(inventory, filename="export_inventory.csv"):
    with open(filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=" ", quoting=csv.QUOTE_NONE, escapechar=" ")
        row = ""
        for key, count in inventory.items():
            row = (key + ",") * count
            writer.writerow([row])
# TESTS-----------------------------------------------------------------------------------------
#_inventory = {}
#_inventory = import_inventory(_inventory,"test_inventory.csv")
# print_table(_inventory)
#random_loot = {"gold":1 , "silver":2, "torch" : 5}
#_inventory = add_to_inventory(_inventory, random_loot)
# print_table(_inventory,"count,asc")
#random_loot2 = ("gold","silver","gold")
#_inventory = add_to_inventory(_inventory, random_loot2)
# print_table(_inventory,"count,desc")
