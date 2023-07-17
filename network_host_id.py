# determines what network id a subnet has and what the host bits are
"""
Class A: 1.0.0.0 to 127.255.255.255
Class B: 128.0.0.0 to 191.255.255.255
Class C: 192.0.0.0 to 223.255.255.255
Class D: 224.0.0.0 to 239.255.255.255
Class E: 240.0.0.0 to 255.255.255.255
"""

import dec_bin_ip_conv
import re

decimal_to_binary = dec_bin_ip_conv.decimal_to_binary_ip
binary_to_decimal = dec_bin_ip_conv.binary_to_decimal_ip

sub = "255.255.224.0"
gate = "192.168.224.1"

# takes gateway and subnet then returns the network id
def network_id(gateway,subnet):
    dec_net_id = ""
    bin_net_id = ""

    # determine length of locked bit in subnet
    sub_len = subnet_length(subnet)
    
    # lock in bits, remove host bits, prepend 0 to host bits, convert back to decimal
    binary_ip = decimal_to_binary(gateway)[:sub_len]
    for i in range(sub_len,32):
        binary_ip += "0"

    dec_net_id = binary_to_decimal(binary_ip)

    return dec_net_id

# returns host bits
def host_bits(net_id,subnet):
    # regex "0"*$, grab that pattern, get length of it flip bits
    # substring net_id in binary[:len(net_id-dif)]
    # put the substrings together, convert back to decimal

    length_of_subnet = subnet_length(subnet)
    #hosts = 32 - length_of_subnet

    bin_net_id = decimal_to_binary(net_id)[:length_of_subnet]
    hosts = bin_net_id

    for i in range(length_of_subnet,32):
        hosts += "1"

    return binary_to_decimal(hosts)

# will need to add regex to ensure the pattern is ^"1"*"0"*$ len(subnet) == 32 
def subnet_length(subnet):
    #print(decimal_to_binary(subnet))
    return len(decimal_to_binary(subnet).strip("0"))

dec_network_id = network_id(gate,sub)
end_of_range = host_bits(dec_network_id,sub)

print("Gateway:\t" + gate + "\nSubnet Mask:\t" + sub + "\nNetwork ID:\t" + dec_network_id)
print("Gateway:\t" + decimal_to_binary(gate) + "\nSubnet Mask:\t" + decimal_to_binary(sub) + "\nNetwork ID:\t" + decimal_to_binary(dec_network_id))
print("Host range:\t" + dec_network_id + " - " + end_of_range)