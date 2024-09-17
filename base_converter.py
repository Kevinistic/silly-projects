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

    number_digits = len(input_number)
    reversed_number = input_number[::-1]

    base36_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    main_number = 0
    for i in range(0, number_digits):
        index_number = base36_list.find(reversed_number[i])
        test = index_number * (base_a ** i)
        main_number += test

    highest_exp = 0

    while main_number > base_b**highest_exp:
        highest_exp += 1

        if main_number < base_b**highest_exp:
            highest_exp -= 1
            break

    results_list = []

    while True:
        counter = 0
        while main_number >= base_b**highest_exp:
            main_number = main_number - base_b**highest_exp
            counter += 1
        results_list.append(base36_list[counter])
        if main_number == 0 and base_b**highest_exp == base_b:
            results_list.append("0")
        highest_exp -= 1
        if main_number == 0:
            break

    results_string = ''.join(results_list) # easter egg
    print(f"Your final result is {results_string}.")
    if results_string == "0" and input_number != "0":
        print("i think you fucked up..")

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