def allOnes(n: int):
    sum = 0
    for i in range(n):
        sum += 2 ^ i
    return sum


def updateBits(n: int, m: int, i: int, j: int):
    right = (~0 << (j + 1))
    print(bin(right))
    left = (1 << i) - 1
    print(bin(left))
    mask = (-right | left)
    print(bin(mask))
    print(bin(~mask))


    n_cleared: int = n & ~(~mask)
    print(bin(n_cleared))

    m_shifted: int = m << i

    print(n_cleared)
    print(m_shifted)

    return n_cleared | m_shifted


if __name__ == '__main__':
    ret = updateBits(0b1000000000000, 0b10011, 2, 6)
    guess = 0b10001001100
    print(guess)
    assert ret == guess
