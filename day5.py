def max_subarrays_sum_k(arr,k) :
    n = len(arr) 
    if n < k :
        return None
    
    window_sum = sum(arr[ : k])
    max_sum = window_sum
    
    for i in range(k,n) :
        window_sum = window_sum + arr[i] - arr[i-k]
        max_sum = max(window_sum,max_sum)
    return max_sum

check = max_subarrays_sum_k([2,1,5,1,3,2],3)
print(check)