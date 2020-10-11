def sort_string(input_str: str) -> str:
    """
    sort space separated string keeping case intact
    :param input_str: string of words, separated by space
    :return: string of words, sorted alphabetically
    """
    return ' '.join(sorted(input_str.split(), key=str.casefold))  # casefold method is used for case-less matching


if __name__ == "__main__":
    # test cases
    assert sort_string("car") == "car"
    assert sort_string("test set") == "set test"
    assert sort_string("apple strawberry banana") == "apple banana strawberry"
    assert sort_string("what is this") == "is this what"
    assert sort_string("weird sentences WEIRD") == "sentences weird WEIRD"
    assert sort_string("apple APPLE strawberry 123 BANANA ORANGE") == "123 apple APPLE BANANA ORANGE strawberry"
