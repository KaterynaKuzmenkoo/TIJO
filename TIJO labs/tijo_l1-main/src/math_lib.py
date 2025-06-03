def max(digits):
    if digits is None or not digits:
        return None
    max_el = digits[0]
    if max_el is None:
        return None
    for num in digits:
        if num is None:
            return None
        if num > max_el:
            max_el = num
    return max_el

def is_perfect(digit):
    sum_of_divisors = 0
    for i in range(1, digit):
        if digit % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == digit