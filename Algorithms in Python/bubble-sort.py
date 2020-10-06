
# Sorting function
def bubbleSort(arr):
    size = len(arr)
    for i in range(size - 1):
        for j in range (0, size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

n = int(input("Enter size : "))
arr = list()
print("Enter elements : ")
for i in range(0, n):
    element = int(input())
    arr.append(element)

arr = bubbleSort(arr)
print("Sorted : ",arr)

# Aims to push all heavy elements in the right side and lighier to the extreme left.
# Best case : Ω(n)
# Worst case : O(n^2)

def main():

    # array takes in space separated numbers from the user
    array = list(
        map(int, input("Enter the numbers separated with space: ").strip().split(" ")))

    output = bubble_sort(array)
    print(f"The sorted array is: {output}")


def bubble_sort(array):

    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[i] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


if __name__ == "__main__":
    main()

