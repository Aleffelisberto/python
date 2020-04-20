def createBinaryRep(n):
    binary = []
    while n != 0:
        binary.append(n % 2)
        n //= 2
    return binary

def maxConsecutive1s(binary):
    max_sequence = 0
    sequence = 0
    for i in binary:
        if i == 1:
            sequence += 1
            if sequence > max_sequence:
                max_sequence = sequence
        else:
            sequence = 0
    
    return max_sequence



def main():
    n = int(input())
    binary = createBinaryRep(n)
    print(maxConsecutive1s(binary))


if __name__ == "__main__":
    main()
