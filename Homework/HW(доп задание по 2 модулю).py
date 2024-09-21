def prizbox(number):
    unique = ''
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                unique += str(i) + str(j)
    return f'{number} - {unique}\nВы прошли'

n = int(input("Введите число: "))

result = prizbox(n)
print(result)
