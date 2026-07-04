def kaprekar(n):
    magic_number = 6174
    current_number = 0
    routine_counter = 0
    new_number = n
    while magic_number != new_number:
        current_number = new_number
        large_number = "".join(sorted(str(current_number), reverse = True))
        small_number = large_number[::-1]
        new_number = int(large_number) - int(small_number)
        routine_counter += 1
        print(large_number, small_number, new_number, routine_counter)
    return routine_counter