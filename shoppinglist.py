shopping_list = ["apple", "bread", "milk", "cheese"]
item_found = False

while item_found == False:
    item = input("Search for an item in your list (or 'q') to quit): ")
    if item.lower() == 'q':
        break
    if item in shopping_list:
        item_found = True
        print(f"{item} found is on your shopping list")

    else:
        print(f"{item} is not on your list")
