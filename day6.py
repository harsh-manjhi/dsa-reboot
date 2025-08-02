def sorted_square(arr) :
    if not arr :
        return []
    n = len(arr)
    result = [0]*n
    left = 0
    right = n - 1
    pos = n-1
    while left <= right :
        if abs(arr[left]) > abs(arr[right]) :
            result[pos] = arr[left] ** 2
            left +=1
        else :
            result[pos] = arr[right] ** 2
            right -= 1
        pos -= 1
    return result

check = sorted_square([-4,-1,0,3,10])
print(check)

# LeetCode 977 - Squares of Sorted Array 
# Approach : Two Pointers (Fill from End)
# Time : O(n), Space : O(n)