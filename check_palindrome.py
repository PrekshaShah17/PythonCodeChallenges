def check_palindrome(input_str: str) -> bool:
    """
    determine whether or not input string is palindrome
    :param input_str: string to evaluate
    :return: boolean value: true
    """
    input_str = input_str.replace(" ", "")  # removing spaces
    reverse_str = input_str[::-1]  # reverse string with slicing
    if input_str == reverse_str:
        return 1
    return 0


if __name__ == "__main__":
    # test cases
    assert check_palindrome("car") == 0
    assert check_palindrome("test set") == 1
    assert check_palindrome("race car") == 1
    assert check_palindrome("what is this") == 0
