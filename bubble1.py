def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Read 8 numbers from the keyboard
arr = []
for _ in range(8):
    num = int(input("Enter a number: "))
    arr.append(num)

# Sort the numbers using Bubble Sort
bubble_sort(arr)
print("Sorted array:", arr)
