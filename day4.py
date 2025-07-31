def move_zeroes(arr) :
    if len(arr) == 0:
        return arr
    
    left = 0
    for right in range(len(arr)) :
        if arr[right] != 0 :

            arr[left], arr[right] = arr[right], arr[left]
            '''temp = arr[right]
            arr[right] = arr[left]
            arr[left] = temp '''
            left += 1
    return arr

print(move_zeroes([0, 0, 0]))  # Expected: [0, 0, 0]
