def draw_line(screen: [bytes], width: int, x1: int, x2: int, y: int):
    start_offset = x1 % 8
    first_full_byte = int(x1 / 8)
    if start_offset != 0:
        first_full_byte += 1

    end_offset = x2 % 8
    last_full_byte = int(x2 / 8)
    if end_offset != 7:
        last_full_byte -= 1

    for b in range(first_full_byte, last_full_byte):
        screen[(width / 8) * y + b] = 0xff

    start_mask = 0xff >> start_offset
    end_mask = (0xff ^ (0xff >> end_offset + 1))
    print(bin(end_mask))

    if start_offset != 0:
        print((width / 8) * y + first_full_byte - 1)
        byte_number = int((width / 8) * y + first_full_byte - 1)
        screen[byte_number] = start_mask | screen[byte_number]

    if end_offset != 7:
        byte_number = int((width / 8) * y + last_full_byte + 1)
        screen[byte_number] = end_mask | screen[byte_number]

    return screen

if __name__ == '__main__':
    screen = draw_line([0 for _ in range(16)], 16, 2, 9, 1)
    print(screen)
    for i in screen:
        print(bin(i))