def is_palindrome(arr):
    if not arr :
        return False
    
    low, high = 0 , len(arr) - 1
    while low < high :
        if arr[low] != arr[high] :
            return False

        low += 1
        high -= 1
    
    return True

check = is_palindrome([1,2,3,2,1])
print(check)