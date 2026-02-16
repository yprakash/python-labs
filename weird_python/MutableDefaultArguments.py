def add_item(item, items=[]):
   items.append(item)
   return items

def add_item2(item, items=None):
   if items is None:
       items = []
   items.append(item)
   return items

print(add_item(1))  # Output: [1]
print(add_item(2))  # Output: [1, 2], not [2] as you might expect
print(add_item2(1))
print(add_item2(2))
