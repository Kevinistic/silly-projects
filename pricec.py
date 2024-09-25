amount_memory = 0
price_memory = 0
rate_memory = 0

while True:
    amount_entry = input("Enter the item amount: ")
    price_entry = input("Enter the price: ")

    amount_temp = int(amount_entry)
    price_temp = int(price_entry)
    rate_temp = price_temp/amount_temp

    if rate_temp > 0 and rate_memory == 0: # assign all temps to memory
        rate_memory = rate_temp
        amount_memory = amount_temp
        price_memory = price_temp
    elif rate_temp > 0: # successful case
        if rate_memory > rate_temp:
            rate_memory = rate_temp
            amount_memory = amount_temp
            price_memory = price_temp
    
    most_worth = print(f"The most worth: {price_memory}/{amount_memory} ({rate_memory})")
    previous = print(f"Previous one: {price_temp}/{amount_temp} ({rate_temp})\n")
    