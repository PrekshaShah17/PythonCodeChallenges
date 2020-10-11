import re


def check_palindrome(input_str: str) -> bool:
    """
    determine whether or not input string is palindrome
    :param input_str: string to evaluate
    :return: boolean value: true
    """
    # removing spaces and special character, converting to lower case
    input_str = re.sub('[\W_]+', '', input_str.lower())
    reverse_str = input_str[::-1]  # reverse string with slicing
    return input_str == reverse_str


if __name__ == "__main__":
    # test cases
    assert not check_palindrome("car")
    assert check_palindrome("test set")
    assert check_palindrome("race car")
    assert not check_palindrome("what is this")
    assert check_palindrome("Go hang a salami - I'm a lasagna hog")
    assert check_palindrome("test123321tset")
