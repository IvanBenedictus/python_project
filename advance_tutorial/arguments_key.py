# *args     = allows you to pass multiple non-key arguments (type: tuple)
# **kwargs  = allows you to pass multiple keyword-arguments (type: dictionary)

# ARGS example 1
def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total
    
print(add(1, 2, 3, 4))

# ARGS example 2
def display_name(*args):
    name = " ".join(args)
    print(f"Hello, {name}")

display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")

# KWARGS
def print_address(**kwargs):
    value = " ".join(kwargs)
    print(value)

print_address(street="123 Fake St.",
              pobox="P.O Box 777",
              city="Detroit",
              state="MI",
              zip="54321")

# Exercise
def shipping_label(*args, **kwargs):
    name = " ".join(args)
    print(name)

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants",
               street="123 Fake St.",
               pobox="PO box #1001",
               city="Detroit",
               state="MI",
               zip="54321")