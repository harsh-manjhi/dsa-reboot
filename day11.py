def LongestStrNonRepeating(s:str) -> int :
    char_index_map = {}
    max_len = 0
    start = 0
    for end in range(len(s)) :
        char = s[end]

        if char in char_index_map and char_index_map[char] >= start :
            start = char_index_map[char] + 1

        char_index_map[char] = end
        max_len = max(max_len, end - start + 1)
    return max_len

check = LongestStrNonRepeating('abcdabdc')
print(check)
