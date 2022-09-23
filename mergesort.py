def mergesort(array):
    debug_print(array=array)
    if len(array) <= 1:
        return array

    m = len(array) // 2
    debug_print(m=m)

    left = mergesort(array[:m])
    right = mergesort(array[m:])

    return merge(left, right)


def merge(left, right):
    debug_print(debug_msg="Merging...", left=left, right=right)

    merged = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    if len(left) > 0:
        merged += left
    else:
        merged += right

    debug_print(merged=merged)
    return merged

