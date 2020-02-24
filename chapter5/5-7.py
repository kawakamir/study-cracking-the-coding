def swap_odd_even_bits(input: int) -> int:
    return ((input & 0xaaaaaaaa) >> 1) | ((input & 0x55555555) << 1)


if __name__ == '__main__':
    input = 55
    print(bin(input))
    print(bin(swap_odd_even_bits(input)))
