def is_balanced(s : str) -> bool :
    stack = []
    mapping = { ')':'(', '}':'{', ']':'[','>':'<', '*':'*'}

    for c in s :
        
        if c in mapping.values() : # Opening bracket
            stack.append(c)

        else : # Closing bracket
            if not stack : return False
            if stack[-1] == mapping[c] :
                stack.pop()
            else : return False

    if len(stack) == 0 : return True
    else : return False

check = is_balanced("()[]{}")
print(check)