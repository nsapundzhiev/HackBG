def factorial(n):
    if n < 1:
        raise ValueError

    fact = 1
    while n > 1:
        fact *= n
        n -= 1
    return fact

def fibonacci(n):

    first = 0
    second = 1
    result = []

    for each in range(n):
        next_number = first + second
        first = second
        second = next_number
        result.append(first)
    return result

def sum_of_digits(n):
    n = abs(n)
    sum = 0
    while n > 0:
        sum += n%10
        n = (int) (n / 10)
    return sum

def fact_digits(n):
    n = abs(n)
    sum = 0
    while n>0:
        sum += factorial(n%10)
        n = (int) (n/10)
    return sum

def palindrome(obj):
    return str(obj)[::-1] == str(obj)

def to_digits(n):
    list_of_digits = []
    while n > 0:
        list_of_digits.append(n%10)
        n = (int) (n/10)
    list_of_digits.reverse()
    return list_of_digits

def to_number(digits):
    result = ""
    for i in digits:
        result += str(i)
    return int(result)

def fib_number(n):
    return to_number(fibonacci(n))

def count_vowels(str):
    count = 0
    vowels = 'aAeEiIoOuUyY'
    for i in str:
        if i in vowels:
            count += 1
    return count

def count_consonants(string):
    count = 0
    symbols = 'bcdfghjklmnpqrstvwxz'
    string  = string.lower()
    for i in string:
        if i in symbols:
            count += 1
    return count

def char_hisrogram(string):
    result = {}
    for i in string:
        if i not in result:
            result[i] = 1
        else:
            result[i] += 1
    return result

def p_score(n):
    result = 0
    palindrome = int(str(n)[::-1])
    if n == palindrome:
        result += 1
    else:
        return 1 + p_score(n + palindrome)
    return result

def is_increasing(seq):
    if len(set(seq)) == 1 and len(set(seq)) != len(seq):
        return False
    return seq == sorted(seq)

def is_decreasing(seq):
    if len(set(seq)) == 1 and len(set(seq)) != len(seq):
        return False
    return seq == sorted(seq, reverse = True)

def hack_number(n):
    bin_n = bin(n)[2:]
    count = str(bin_n).count('1')
    return bin_n == bin_n[::-1] and count % 2 != 0

def next_hack(n):
    n += 1
    if hack_number(n):
        return n
    return next_hack(n)
