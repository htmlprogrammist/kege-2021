caramel = [[-1, 3, 7, 8, 0], [7, 8, -1, 3, 1], [1, 3, 0, 8, 3], [0, 1, 3, 7, -1]]
"""
{-1: [(0, 1, 3), (0, 2, 4)], 3: [(0, 1, 2, 3), (1, 2, 3, 4)], 7: [(0, 1, 3), (0, 2, 3)], 8: [(0, 1, 2), (1, 3)], 0: [(0, 2, 3), (0, 2, 4)], 1: [(1, 2, 3), (0, 1, 4)]}
"""
x = 0
y = 0
# Получение каждого отдельного элемента
while y <= len(caramel):
    current_list_item = caramel[x][y]
    itie = []
    jtie = []
    result = []
    for i in range(len(caramel)):
        for j in range(len(caramel[i])):
            # print(caramel[i][j])
            if caramel[i][j] == current_list_item:
                itie.append(i)
                jtie.append(j)
    result.append(tuple(itie))
    result.append(tuple(jtie))
    x += 1
    y += 1
    print({current_list_item: result})
