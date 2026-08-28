def is_number_palindrome(number, divisor=None):
    if divisor is None:
        divisor = 1

    while number // divisor >= 10:
        divisor *= 10

    if number < 10:
        return True

    first = number // divisor
    last = number % 10

    if first != last:
        return False

    number = (number % divisor) // 10

    return is_number_palindrome(number, divisor // 100)

print(is_number_palindrome(12321))