def decimal_binary(number):
    mostbit = 128
    bits = [0,0,0,0,0,0,0,0]
    byte = ""
    for i in range(0,len(bits)):
        #print(mostbit)
        if (number - mostbit >= 0):
            #print(str(number) + " - " + str(mostbit) + " >= 0: " + str(number - mostbit))
            number = number - mostbit
            bits[i] = 1
        elif(number - mostbit < 0):
            #print(str(number) + " - " + str(mostbit) + " < 0: " + str(number - mostbit))
            bits[i] = 0
        mostbit = mostbit/2

    for bit in bits:
        byte += str(bit)
    return byte

def binary_decimal(number):
    mostbit = 128
    byte = 0
    for i in number:
        byte += int(i) * mostbit
        mostbit = mostbit/2

    return str(int(byte))

#print(decimal_binary(192))

#print(binary_decimal("11110000"))