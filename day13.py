 # Problem 1
def MaxSubarrSum(arr , k) -> int :
    n = len(arr)

    if k > n :
        return -1
    if not arr :
        return None
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k,n) :
        window_sum = window_sum + arr[i] - arr[i - k]
        max_sum = max(max_sum,window_sum)
    return max_sum

check = MaxSubarrSum([1,1,1,1,1],3)
print(check)

 # Problem 2
def LongestStrWithoutRepeat(s : str) -> int :
    char_index_map = {}
    start = 0
    max_len = 0
    for end in range(len(s)) :
        char = s[end]
        if char in char_index_map and char_index_map[char] >= start :
            start = char_index_map[char] + 1
        char_index_map[char] = end
        max_len = max(max_len, end - start + 1)
    print(char_index_map)
    return max_len
check = LongestStrWithoutRepeat('qqqqqq')
print(check)

 # Problem 3
def SubarrSumK(arr, k) -> int :
    prefix_map = {0 : 1}
    curr_sum = 0
    count = 0
    for num in arr :
        curr_sum += num
        
        if (curr_sum - k) in prefix_map :
            count += prefix_map[curr_sum - k]
        prefix_map[curr_sum] = prefix_map.get(curr_sum,0) + 1
    print(prefix_map)
    return count
     
check = SubarrSumK([1,2,3,4,5],5)
print(check)


 # Problem 4
def MinSubarrLengthk(arr, k) -> int :
    curr_sum = 0
    min_len = float("inf")
    left = 0
    for right in range(len(arr)) :
        curr_sum += arr[right]
        while curr_sum >= k : 
            min_len = min(min_len, right - left + 1)
            curr_sum -= arr[left]
            left += 1
    return min_len


check = MinSubarrLengthk([2,3,2,5,4,9],5)
print(check)