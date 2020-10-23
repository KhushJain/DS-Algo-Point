def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
   
arr = [64, 34, 25, 12, 22, 11, 90] 
  
bubbleSort(arr) 
  
print("Sorted array is:") 
for i in range(len(arr)): 
    print(arr[i])


"""
Problem : Sort the given array using bubble sort.

Traverse through all elements of array and in each pass place the element having maximum value at last of unsorted array. After each pass length of unsorted elements decreases hence we don't have to traverse all elements in every pass.

Sample I/O:

Enter number of elements:5
Enter elements:
5
4
3
2
1
Sorted array is:
[1, 2, 3, 4, 5]

Enter number of elements:4
Enter elements:
2
4
1
3
[1, 2, 3, 4]

Time complexity: O(n^2) (worst)
Space complexity: O(1)
"""
