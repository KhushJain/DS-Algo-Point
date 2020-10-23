def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
  
arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 
for i in range(len(arr)): 
    print(arr[i]) 

"""
I/O:
Enter Data: 9, 5, 1, 4, 3
Sorted Array in Ascending Order:
[1, 3, 4, 5, 9]

Complexities:
Time Complexities:
Worst Case Complexity: O(n^2)
Best Case Complexity: O(n)
Average Case Complexity: O(n^2)

Space Complexities:
Space complexity is O(1) because an extra variable key is used.
"""
