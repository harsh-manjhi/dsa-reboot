def Longest_subarr_atmost_2_k_unique(fruits , k) :
    if not fruits : return 0
    count = {}
    l, max_len = 0, 0

    for r in range(len(fruits)) :

        count[fruits[r]] = count.get(fruits[r],0) + 1

        while len(count) > k :

            count[fruits[l]] -= 1
            
            if count[fruits[l]] == 0 :
                count.pop(fruits[l])

            l += 1

        max_len = max(max_len, r - l + 1)
        
    return max_len

check = Longest_subarr_atmost_2_k_unique([1, 2, 1, 2, 3],2)
print(check)