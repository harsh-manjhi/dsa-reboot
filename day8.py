def min_subarr_len(arr,target) :
    if not arr :
        return 0
    
    left = 0
    window_sum = 0
    min_len = float("inf")

    for right in range(len(arr)) :
        window_sum += arr[right]

        while window_sum >= target :
            min_len = min(min_len, right - left + 1)
            window_sum -= arr[left]
            left += 1

    return 0 if min_len == float("inf") else min_len

check = min_subarr_len([10,2,3],7)
print(check)