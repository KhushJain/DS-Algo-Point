""" Python program for implementation of Quicksort Sort
 This function takes last element as pivot, places
 the pivot element at its correct position in sorted
 array, and places all smaller (smaller than pivot)
 to left of pivot and all greater elements to right
 of pivot"""


def partition(arr,low,high): 
    i = ( low-1 )
    pivot = arr[high] 
  
    for j in range(low , high): 
        if   arr[j] < pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])

"""
  Input/Output
    enter the length of array 5
    enter the elements of the array
    10
    6
    8
    2
    4
    unsorted array is
    [10, 6, 8, 2, 4]
    Sorted array is:
    [2, 4, 6, 8, 10]
   SPACE COMPLEXITY:
   Solution: Quicksort has a space complexity of O(logn), even in the worst case.
   TIME COMPLEXITY
   time complexity in worst case is  O(n^2).
"""
