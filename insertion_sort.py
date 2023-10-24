# Insertion sort on an array

def insertion_sort(array):
    for i in range(1, len(array)):
        value = array[i]
        j = i - 1
        while j >= 0 and array[j] < value:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = value


integers = []

for number in range(5):
    integer = int(input("Enter integer {}: ".format(number + 1)))
    integers.append(integer)
insertion_sort(integers)

print("Sorted list: ", end='')
for integer in integers:
    print(integer, end='  ')
