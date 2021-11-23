def odd_nums(n):
    for num in range(1, n + 1):
        if num % 2 > 0:
            yield num


odd_to_15 = odd_nums(15)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print('-' * 50)
n = int(input('n = : '))
odd_to_15 = (num for num in range(1, n + 1) if num % 2 > 0)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print('*'* 100)