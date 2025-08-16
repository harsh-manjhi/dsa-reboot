def NextGreaterElement(arr) :
    n = len(arr)
    stack = []
    result = [-1] * n 

    for i in range(n-1, -1, -1) :

        while stack and stack[-1] <= arr[i] :   #Disturbed decreasing order
            stack.pop()     # pop the value

        if stack :
            result[i] = stack[-1]

        stack.append(arr[i])
    
    return result

check = NextGreaterElement([4, 5, 2, 25])
print(check)