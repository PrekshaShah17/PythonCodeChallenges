def search_indices(search_list: list, goal: int) -> list:
    """
    find indices of the goal from the list
    :param search_list: list to search
    :param goal: value to search for
    :return: list with indexes
    """
    indices = []
    for i in range(len(search_list)):
        if search_list[i] == goal:
            indices.append([i])
        elif isinstance(search_list[i], list):  # to check if we have sub list
            for sub_i in search_indices(search_list[i], goal):
                indices.append([i]+sub_i)
    return indices


if __name__ == "__main__":
    # test cases
    assert search_indices([1, 2, 3], 3) == [[2]]
    assert search_indices([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2) == [[0, 0, 1], [0, 1], [1, 1]]
    assert search_indices([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], [1, 2, 3]) == [[0, 0], [1]]