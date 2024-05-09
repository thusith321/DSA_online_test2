def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Take user input for 5 numbers
print("Please enter 5 numbers separated by spaces:")
numbers = input().split()[:5]  # Take only the first 5 numbers if more than 5 are entered
numbers = [int(num) for num in numbers]

print("Unsorted numbers:", numbers)

insertion_sort(numbers)

print("Sorted numbers:", numbers)
