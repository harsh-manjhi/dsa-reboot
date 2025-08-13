def minwindow_substr(s :str, t: str) :
    if s == "" : return ""

    window, countT = {}, {}
    for c in t :
        countT[c] = countT.get(c,0) + 1

    have, need = 0, len(countT)
    l = 0
    res, resLen = [-1, -1], float("inf")

    for r in range(len(s)) :
        c = s[r]
        window[c] = window.get(c,0) + 1

        if c in countT and window[c] == countT[c] :
            have += 1
        
        while have == need :

            if (r - l + 1) < resLen :
                res = l,r
                resLen = (r - l + 1)
            
            window[s[l]] -= 1

            if s[l] in countT and window[s[l]] < countT[s[l]] :
                have -= 1
            
            l += 1

    l,r = res

    return "" if resLen == float("inf") else s[l : r+1]

check = minwindow_substr("ADOBECODEBANC","ABC")
print(check)