def binary_search(list, item):
    """
    :param list: The sorted array as list
    :param item: The element to be found in the list
    :return: Returns element if found else None
    """
    size = len(list)
    if size <= 0:
        return None
    start = 0
    end = size - 1
    while (start <= end):
        mid = int((start + end) / 2)
        if item == list[mid]:
            return list[mid]
        if item < list[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None
