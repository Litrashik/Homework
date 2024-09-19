def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        list_ = []
        for j in range(m):
            list_.append(value)
        matrix.append(list_)
    return matrix

result1 = get_matrix(4, 1, 156)
result2 = get_matrix(6, 3 , 312)
result3 = get_matrix(2, 5, 624)
print(result1)
print(result2)
print(result3)
