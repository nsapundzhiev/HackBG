def sum_all_divisors(n):
    return sum([i for i in range(1,n+1) if n % i == 0])

def is_prime(n):
    count = 0

    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    return count == 2

def count_all_divisors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

def prime_number_of_divisors(n):
    return is_prime(count_all_divisors(n))

def to_digits(n):
    list_of_digits = []
    while n > 0:
        list_of_digits.append(n%10)
        n = int (n/10)
    list_of_digits.reverse()
    return list_of_digits

def contains_digit(number, digit):
    return digit in to_digits(number)


def contains_digits(number, digits):
    count = 0
    number_to_list = to_digits(number)
    for i in digits:
        for j in set(number_to_list):
            if i == j:
                count += 1
    return count >= len(digits)


def is_number_balanced(n):

    listt = to_digits(n)
    length = len(listt) / 2

    if len(listt) % 2 == 0:
        return sum(listt[:length]) == sum(listt[length:])
    else:
        return sum(listt[:length +1 ]) == sum(listt[length:])


def count_substrings(haystack, needle):
    return haystack.count(needle)


def to_number(digits):
    result = ""
    for i in digits:
        result += str(i)
    return int(result)


def zero_insert(n):

    result = []
    n_list = to_digits(n)
    i = 0

    while i < len(n_list) - 1 :
        result.append(n_list[i])
        if n_list[i] == n_list[i+1] or (n_list[i] + n_list[i+1]) % 10 == 0:
            result.append(0)
        i += 1
    result.append(n_list[i])

    return to_number(result)


def sum_matrix(m):
    total = 0
    for i in m:
        total += sum(i)
    return total
