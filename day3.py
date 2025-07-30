def remove_duplicates(arr) :
    if len(arr) == 0 :
        return 0
    slow = 0
    for fast in range(1, len(arr)) :
        if arr[fast] != arr[slow] :
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1

check = remove_duplicates([1,1,1,2,2,3,3])
print(check)