def LongestCharReplacement(s : str,k : int) -> int :
    count = {}
    result = 0
    left = 0
    max_freq = 0

    for right in range(len(s)) :
        char = s[right]
        count[char] = count.get(char,0) + 1

        max_freq = max(max_freq,count[char])
        
        if (right - left + 1) - max_freq > k :
            count[s[left]] -= 1
            left += 1

        
        result = max(result, right - left + 1)
    
    print(count)
    return result

check = LongestCharReplacement('ABABBA',2)
print(check)

        