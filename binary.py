def solution(N):

    binary_number = bin(N)
    count = -1
    maximum = 0
    for index in range(len(binary_number)):
        if binary_number[index] == "0":
            count += 1
        elif binary_number[index] == "1" and count > maximum:
            maximum = count
            count = 0
    return maximum





