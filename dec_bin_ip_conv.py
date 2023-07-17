from ipaddress import ip_address
import decimal_binary_octet_conv

ip_address = "192.168.1.10"
bd = decimal_binary_octet_conv.decimal_binary
db = decimal_binary_octet_conv.binary_decimal
# read in string x.x.x.x
# or read from 4 separate octets
# turns decimal ip address into binary
def decimal_to_binary_ip(ip_addr):
    binary_address = ""

    for i in range(0,4):
        octet = ip_addr.split(".")[i]
        binary_address += str(bd(int(octet)))

    return binary_address


#print(decimal_to_binary_ip(ip_address))

def binary_to_decimal_ip(ip_addr):
    decimal_address = ""
    decimal_address += db(ip_addr[:8]) + "."
    decimal_address += db(ip_addr[8:16]) + "."
    decimal_address += db(ip_addr[16:24]) + "."
    decimal_address += db(ip_addr[24:32])

    return decimal_address

#print(binary_to_decimal_ip("11000000101010000000000100001010"))