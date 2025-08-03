def longest_subarr_sum_leq_k(arr,k) :
    if not arr :
        return 0
    left = 0
    window_sum = 0
    max_len = 0

    for right in range(len(arr)) :
        # Sliding Window
        window_sum = window_sum + arr[right]
        # Checking if window_sum is leq k
        while window_sum > k and left <= right :
            window_sum = window_sum - arr[left]
            left += 1
        # Maximum length 
        max_len = max(max_len,right - left + 1)

    return max_len

check = longest_subarr_sum_leq_k([2,1,5,2,3,2],7)
print(check)
