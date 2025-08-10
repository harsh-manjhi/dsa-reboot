# Probelem 1
def Two_sum(arr, k) :
    if not arr :
        return None
    
    left = 0
    right = len(arr) - 1
    while left < right :
        sum = arr[left] + arr[right]
        if sum == k :
            return True
        elif sum > k :
            right = right - 1
        else :
            left = left + 1
    return False

check = Two_sum([2,3,4,5,6,7],8)
print(check)


 # Problem 2
def max_subarr_sum(arr, k) :
    n = len(arr)
    if k > n :
        return None
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k,n) :
        window_sum = window_sum + arr[i] - arr[i - k]
        max_sum = max(max_sum,window_sum)
    return max_sum

check = max_subarr_sum([-5,-2,-1,-9,-7],2)
print(check)
   

# Problem 3
def longest_substr_non_repeating(s : str) -> int :
    max_len = 0
    left = 0
    char_index_map = {}
    for right in range(len(s)) :
        char = s[right]
        if char in char_index_map and char_index_map[char] >= left  :
            left = char_index_map[char] + 1
        
        char_index_map[char] = right
        max_len = max(max_len,right - left + 1)
    return max_len
    
check = longest_substr_non_repeating('abcab')
print(check) 