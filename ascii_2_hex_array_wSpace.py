#! /usr/bin/env python3 
######################################################################
## Quick convert strings to Hex w. space
##
## Insert your string in the string field
##
######################################################################

import binascii

string  = '''   '''

encoded_string = string.encode("UTF-8")
unformatted_hex_array = encoded_string.hex()
hex_array_split_on_two_pattern = ' '.join(unformatted_hex_array[i:i + 2] for i in range(0, len(unformatted_hex_array), 2))
print(hex_array_split_on_two_pattern)




