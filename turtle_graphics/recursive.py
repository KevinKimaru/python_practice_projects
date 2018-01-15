# def r3(n):
#     print(n, "Start")
#     if n < 4:
#         r3(n + 1)
#     print(n, "End")

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(8))

def fact_r(n):#Recursive implentation
    if n == 1:
        return 1
    return n * fact_r(n - 1)

print(fact_r(5))

def fact_nr(n):#non-recursive implementation
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

print(fact_nr(4))

def reverse(s):
    if s == "":
        return ""
    return s[-1] + reverse(s[:-1])

print(reverse("Kevin"))

def reverse_help(s, n):
    if n == len(s):
        return ""
    else:
        return reverse_help(s, n + 1) + s[n]

print(reverse_help("kevin", 0))

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) == 0:
            result.extend(right)
            break
        else:
            result.extend(left)
            break
        print(result)
    return result

print(merge([1, 5, 10], [0, 4, 6, 7, 8]))


