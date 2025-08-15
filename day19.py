def min_remove_p_stack(s:str) :
    # s -> list
    stack = []
    chars = list(s)
    # pass 1 - checking ')' unmatched
    for i in range(len(chars)) :
        if chars[i] == '(' :
            stack.append(i)
        elif chars[i] == ')' :
            if stack :
                stack.pop()
            else :
                chars[i] = ''
    
    # pass 2 
    while stack :
        idx = stack.pop()
        chars[idx] = ''

    # rebuild the s 
    result = ""
    for ch in chars :
        if ch != '' :
            result += ch
        
    return result

check = min_remove_p_stack("a)b(c)d")
print(check)