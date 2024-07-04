def code(number):
    result = []
    for i in range(1, number + 1):
        for k in range(i + 1, number + 1):
            sum = i + k
            if number % sum == 0:
                result.append(i)
                result.append(k)
    return result


number = int(input('Введите число в первую ячейку:'))
result = code(number)
print(*result)
