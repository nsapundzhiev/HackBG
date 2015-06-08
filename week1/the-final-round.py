def count_words(arr):
    result = {}
    for i in arr:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result


def unique_words_count(arr):
    return len(count_words(arr))


def nan_expand(times):
    result = ""
    if times < 1:
        return result
    else:
        while times >= 1:
            result += "Not a "
            times -=1
    return result + "NaN"



def iterations_of_nan_expand(expanded):
    if nan_expand(expanded.count("Not a")) == expanded:
        return expanded.count("Not a")
    return False


def to_number(digits):
    result = ""
    for i in digits:
        result += str(i)
    return int(result)

def group(seq):
    result = []
    lis = []
    seq.append("")

    for i in range(len(seq)-1):
        if seq[i] != seq[i+1]:
            lis.append(seq[i])
            result.append(lis)
            lis = []
        else:
            lis.append(seq[i])

    if lis != []:
        result.append(lis)

    if result == []:
        return seq

    return result


def max_consecutive(items):
    seq = group(items)
    max_count = 0
    for i in seq:
        if max_count < len(i):
            max_count = len(i)

    return max_count


def groupby(func, seq):
    result = {}

    for i in seq:
        if func(i) in result:
            result[func(i)].append(i)
        else:
            result[func(i)] = [i]
    return result


def is_prime(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1

    return count == 2

def all_prime_addends(n):
    all_primes = []
    for i in range(1, n+1):
        if is_prime(i):
            all_primes.append(i)
    return all_primes

def goldbach(n):
    result = []
    if n % 2 == 1:
        return False
    else:
        for i in all_prime_addends(n):
            if (i <= n - i) and is_prime(n-i):
                k = (i, n-i)
                result.append(k)
    return result


def to_digits(n):
    list_of_digits = []
    while n > 0:
        list_of_digits.append(n%10)
        n = (int) (n/10)
    list_of_digits.reverse()
    return list_of_digits



def is_credit_card_valid(number):

    if number % 2 == 0:
        return False

    seq = to_digits(number)

    result = [seq[i] for i in range(len(seq)) if i % 2]
    result1 = [seq[i]*2 for i in range(len(seq)) if i % 2]
    result1 = to_digits(to_number(result1))

    total = sum(seq) - sum(result) + sum(result1)

    return total % 10 == 0



def is_an_bn(word):

    if len(word) % 2 != 0:
        return False
    a_half = word[:len(word)/2]
    b_half = word[len(word)/2:]

    if ('a' in b_half) or ('b' in a_half):
        return False

    return word.count("a") == word.count("b")
