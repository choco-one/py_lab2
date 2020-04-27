
def conv():
    input_bin_num = int(input('input binary number : '))
    str_bin_num = str(input_bin_num)
    result = 0

    for i in range(len(str_bin_num)):
        result = ((input_bin_num % (10**(i+1)))//(10**i)) * (2**i) + result

    print('=> OCT > ', format(result, 'o'))
    print('=> DEC > ', format(result, 'd'))
    print('=> HEX > ', format(result, 'X'))
