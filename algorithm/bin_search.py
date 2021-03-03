def bin_search_exist(lst, target):
    """
    :param lst: list of values
    :param target:
    :return: index if target in lst, else -1
    """
    left, right = 0, len(lst)
    while left < right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid
    return -1


def bin_search_insert_index(lst, value):
    """
    find the index to insert the value
    :param lst: list of values
    :param value:
    :return: [0, len(lst)], i if lst[i] >= value, len(lst) if value is bigger than all values in lst
    """
    left, right = 0, len(lst)
    while left < right:
        mid = (left + right) // 2
        if lst[mid] == value:
            return mid
        elif lst[mid] < value:
            left = mid + 1
        else:
            right = mid
    return right
