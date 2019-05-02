def linear_search(list, item):
    """
    :param list: The array of elements as list
    :param item: The element to be found in the list
    :return: Returns element if found else None
    """
    size = len(list)
    if size <= 0:
        return None
    start = 0
    end = size - 1
    while (start <= end):
        if item == list[start]:
            return list[start]
        start=start+1
    return None
