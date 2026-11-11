items = []

n = int(input("How many favourite items do you want to add? "))

for i in range(n):
    item = input("Enter item: ")
    items.append(item)

print("Favourite items:", items)

remove_item = input("Enter item to remove: ")

if remove_item in items:
    items.remove(remove_item)
    print("Item removed successfully")
else:
    print("Item not found")

print("Updated list:", items)