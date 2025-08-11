# Problem 1 :
def max_sum_subarr_k(arr, k) :
    n = len(arr)
    if k > n :
        return None
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k,n) :
        window_sum += arr[i] - arr[i-k]
        max_sum = max(window_sum, max_sum)
    return max_sum

check = max_sum_subarr_k([2,3,2,5,4],3)
print(check)


# Problem 2
def max_consecutive_ones(arr) :
    max_count = 0
    curr_streak = 0
    for num in arr :
        if num == 1 :
            curr_streak += 1
        elif num == 0 :
            curr_streak = 0
        max_count = max(max_count, curr_streak)
    return max_count


check = max_consecutive_ones([1,0,1,1,1,0])
print(check)

# Problem 3
def LongestSubstrWithoutRepeatingChar(s : str) -> int :
    if not s :
        return 0
    char_index_map = {}
    max_len = 0
    left = 0
    for right in range(len(s)) :
        char = s[right]
        if char in char_index_map and char_index_map[char] >= left :
            left = char_index_map[char] + 1
        char_index_map[char] = right 
        max_len = max(max_len, right - left + 1)
    return max_len

check = LongestSubstrWithoutRepeatingChar('abcdadc')
print(check)

# Problem 4
def min_subarr_sum(nums, target) :
    min_len = float("inf")
    curr_sum = 0
    left = 0
    for right in range(len(nums)) :
        curr_sum += nums[right]
        while curr_sum >= target :
            min_len = min(min_len, right - left + 1)
            curr_sum -= nums[left]
            left += 1
    return 0 if min_len == float("inf") else min_len


check = min_subarr_sum([2,3,2,5,4,1],5)
print(check)