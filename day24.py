from collections import deque
def Max_sliding_Window(nums : list[int], k : int) -> list[int] :
    if not nums : return nums

    dq = deque()
    res = []

    for i in range(len(nums)):

        if dq and dq[0] == i - k :
            dq.popleft()
        
        while dq and nums[dq[-1]] < nums[i] :
            dq.pop()

        dq.append(i)

        if i >= k - 1 :
            res.append(nums[dq[0]])

    return res

check = Max_sliding_Window([1,3,-1,-3,5],3)
print(check)
