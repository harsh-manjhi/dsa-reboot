def subarr_sum_k_count(arr, k) :
    if not arr :
        return 0
    count = 0
    prefix_map = {0:1}
    curr_sum = 0
    
    for num in arr :
        curr_sum += num
        need = curr_sum - k

        if (curr_sum - k) in prefix_map :
            count += prefix_map[need]

        prefix_map[curr_sum] = prefix_map.get(curr_sum,0) + 1   
    return count

check = subarr_sum_k_count([1,2,3,-2,5],3)
print(check)
