for N in range(100, 500):
    binary = bin(N)[2:]
    units = binary.count('1')
    zeros = binary.count('0')
    if units == zeros:
        binary += binary[-1]
    else:
        if units < zeros:
            binary += '1'
        else:
            binary += '0'
    units = binary.count('1')
    zeros = binary.count('0')
    if units == zeros:
        binary += binary[-1]
    else:
        if units < zeros:
            binary += '1'
        else:
            binary += '0'
    units = binary.count('1')
    zeros = binary.count('0')
    if units == zeros:
        binary += binary[-1]
    else:
        if units < zeros:
            binary += '1'
        else:
            binary += '0'
    R = int(binary, 2)
    if R % 4 == 0:
        print(N)
        break
