answers = []
condition = 115

for N in range(10000000):
    binary = bin(N)[2:]
    if N % 2 == 0:
        binary += '00'
    else:
        binary += '11'
    # print(binary, answer)
    if int(binary, 2) > condition:
        answers.append(N)

print(max(answers))
