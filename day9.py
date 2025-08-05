def subarr_sum_exists(nums,target) :
    prefix_map = {0:1}
    curr_sum = 0
    for num in nums:
        curr_sum += num
        if (curr_sum - target) in prefix_map :
            return True
        prefix_map[curr_sum] = prefix_map.get(curr_sum,0) + 1
    return False

check = subarr_sum_exists([1,2,-3,4,2],3)
print(check)
