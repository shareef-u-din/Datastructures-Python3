def binary_search(l, item):
    """
    :param list: The sorted array as list
    :param item: The element to be found in the list
    :return: Returns found=1 if element is present and found=0 if not
    """
    size = len(l)
    if size <= 0:
        return None
    start = 0
    end = size - 1
    found = 0
    while (start <= end):
        mid = int((start + end) / 2)
        if item == l[mid]:
            found = 1
            break
        if item < l[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return found
