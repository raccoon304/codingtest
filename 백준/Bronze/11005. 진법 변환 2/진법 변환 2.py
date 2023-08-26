def convert_to_base_n(number, base):
    if number == 0:
        return "0"

    result = ""
    while number > 0:
        remainder = number % base
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(ord('A') + remainder - 10) + result
        number //= base
    
    return result

decimal_number, base = map(int,input().split())

converted_number = convert_to_base_n(decimal_number, base)
print(converted_number)
