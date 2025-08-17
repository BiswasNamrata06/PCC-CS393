def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid   
        elif arr[mid] < target:
            low = mid + 1  
        else:
            high = mid - 1  
            
    return -1  


elements=list(map(int,input("Enter the elements in the list:").split()))
elements.sort()
target = int(input("Enter number to search: "))

result = binary_search(elements, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
