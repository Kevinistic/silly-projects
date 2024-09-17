# converting number from base a to base b
# i will be adding comments on how this work soon.

import math # importing math...

continue_flag = True
while continue_flag: # looping from the very below
    input_number = input("Enter your current number: ").upper() # get main number
    if '-' in input_number:
        print("negative numbers currently unsupported")
        continue
    base_a = input("Enter your current base: ") # get current base
    if not base_a.isdigit():
        print("nuh uh")
        continue
    base_b = input("Enter your desired base: ") # get desired base
    if not base_b.isdigit():
        print("nuh uh")
        continue

    base_a = int(base_a)
    base_b = int(base_b)

    while True: # idiot proof
        if '0' in input_number[0]:
            input_number = input_number[1:]
        elif '0' in input_number[-1]:
            input_number = input_number[:-1]
        else: break

    if '.' not in input_number: # for any X input, convert to X.0
        input_number = input_number + ".0"
    dot = input_number.find('.')
    integer_number = input_number[:dot]
    fraction_number = input_number[dot+1:]

    integer_number_digits = len(integer_number)
    integer_reversed_number = integer_number[::-1]
    fraction_number_digits = len(fraction_number)
    fraction_reversed_number = fraction_number[::-1]

    base36_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    integer_main_number = 0
    for i in range(integer_number_digits):
        index_number = base36_list.find(integer_reversed_number[i])
        test = index_number * (base_a ** i)
        integer_main_number += test
    
    fraction_main_number = 0
    for i in range(fraction_number_digits):
        index_number = base36_list.find(fraction_reversed_number[i])
        test = index_number * (base_a ** -(i+1))
        fraction_main_number += test

    highest_exp = 0
    while integer_main_number > base_b**highest_exp:
        highest_exp += 1
        if integer_main_number < base_b**highest_exp:
            highest_exp -= 1
            break

    results_list = []

    while True:
        counter = 0
        while integer_main_number >= base_b**highest_exp:
            integer_main_number = integer_main_number - base_b**highest_exp
            counter += 1
        results_list.append(base36_list[counter])
        if integer_main_number == 0 and base_b**highest_exp == base_b:
            results_list.append("0")
        highest_exp -= 1
        if integer_main_number == 0:
            break
    
    results_list.append(".")
    lowest_exp = -1
    epsilon = 1e-10
    while True:
        counter = 0
        while fraction_main_number >= base_b**lowest_exp:
            fraction_main_number = fraction_main_number - base_b**lowest_exp
            counter += 1
        results_list.append(base36_list[counter])
        if abs(fraction_main_number) < epsilon and base_b**lowest_exp == base_b:
            results_list.append("0")
        lowest_exp -= 1
        if abs(fraction_main_number) < epsilon:
            break

    results_string = ''.join(results_list) # easter egg
    if results_string[-1] == '0':
        results_string = results_string[:-2]
    print(f"Your final result is {results_string}")

    while True: # continue prompt
        confirm = input("Continue? (Y/N): ")
        if confirm.upper() == 'Y':
            continue_flag = True
            break
        elif confirm.upper() == 'N':
            continue_flag = False
            break
        else: print("nuh uh")

print("Thank you for using my silly base converter")