def find_prime_factor(num: int) -> list:
    """
    function to find prime factors for given input
    :param num: input number (int type)
    :return: list of prime factors. if less than or equal to 0 returns "invalid input" string
    """
    factors, prime = [], 2

    # addressing base and corner cases
    if num == 1:
        return [1]
    if num <= 0:
        return "Invalid input!"

    while prime <= num:  # this will be true when number reaches 1
        if num % prime == 0:  # finding divisors
            factors.append(prime)
            num /= prime  # replacing number with new value for further processing
        else:
            prime += 1  # divisor doesn't divide evenly, moving to next divisor

    return factors


if __name__ == "__main__":
    # test cases
    assert find_prime_factor(1) == [1]
    assert find_prime_factor(3) == [3]
    assert find_prime_factor(2) == [2]
    assert find_prime_factor(13) == [13]
    assert find_prime_factor(26) == [2, 13]
    assert find_prime_factor(650) == [2, 5, 5, 13]
    assert find_prime_factor(-2) == "Invalid input!"
