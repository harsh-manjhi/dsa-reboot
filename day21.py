def daily_temperatures(temps) :
    n = len(temps)
    res = [0] * n
    stack = []
    
    for i in range(n) :
        while stack and temps[i] > temps[stack[-1]] :
            prev = stack.pop()
            res[prev] = i - prev 
        stack.append(i)

    return res

check = daily_temperatures([73,74,75,71,69,72,76,73])
print(check)