# exponent function is the power of function
# for example 2^3 = 8
# we type it as 2**3 in python

print(2**3)
# 1st step is to create a function which include base & power number
def raise_to_power (base_num, pow_number):
    result = 1
    for index in range(pow_number):
        result = result * base_num
    return result

print(raise_to_power(4, 4))
