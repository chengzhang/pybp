# reference to python bisect.bisect_right bisect_left


def bin_search_left(a, x, lo=0, hi=None):
    if not hi:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x <= a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


def bin_search_right(a, x, lo=0, hi=None):
    if not hi:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


def bin_search(a, x, lo=0, hi=None):
    insert_index = bin_search_left(a, x, lo, hi)
    if insert_index == hi:
        return False
    return a[insert_index] == x
