def two_pointers(arr,target) :
    if not arr :
        return False 
    low , high = 0, len(arr) - 1
    while low < high :
        current_sum = arr[low] + arr[high] 
        if current_sum == target :
            return True
        elif current_sum > target :
            high -= 1
        else :
            low += 1
    return False

check = two_pointers([1,2,3,4,5,6,7],8)
print(check)