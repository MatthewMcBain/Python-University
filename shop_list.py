# Output shopping list in numerical order

def sort(data, product):
    for this_index in range(len(data) - 1):
        swap_index = find_smallest(data, this_index)
        if swap_index != this_index:
            swap(data, swap_index, this_index, product)


def find_smallest(sort_data, start_index):
    swap_index = start_index
    for index in range(start_index + 1, len(sort_data)):
        if sort_data[index] > sort_data[swap_index]:
            swap_index = index
    return swap_index


def swap(swap_data, from_index, to_index, product_data):
    swap_data[from_index], swap_data[to_index] =\
        swap_data[to_index], swap_data[from_index]
    product_data[from_index], product_data[to_index] =\
        product_data[to_index], product_data[from_index]


items = []
prices = []

for string_input in range(5):
    strings = input("Enter item name and price: ")
    splits_string = strings.split()

    if len(splits_string) > 2:
        item = ' '.join(splits_string[:-1])
        price = ' '.join(splits_string[-1:])
    else:
        item, price = splits_string
    items.append(item)
    prices.append(price)

sort(prices, items)

print()
print("The sorted prices are:")
for description in range(5):
    print(items[description], prices[description])
