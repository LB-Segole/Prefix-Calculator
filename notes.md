# Build: Python unit prefix converter (input a value + prefix → output in base SI units)

# idea for building """ this whole thing is supposed to convert SI prefixes to base units
# what are base unit? globally agreed measurement system used in all science and engineering 
# Base units: m, kg, s, A(ampere), K(kelvin), mol(mole), cd(candela)
# these are symobols for; length, mass, time, electric current, temperature, amount of substance
# and luminous intensity
# then what are prefixes; A prefix is a word or symbol placed before a unit to indicate a multiple or fraction of that unit.
# Instead of writing 0.000 001 metres we write 1 micrometre (1 µm). Prefixes make measurements readable."""
# Prefixes: giga(G), mega(M), kilo(k), milli(m), micro(µ), nano(n)
# What is an exponent in python? it's not (^), it's (**) or pow(x, y)
# Getting an error from this code: # prefixes = [
# (giga = 10**9),
# (mega = 10**6),
# (kilo = 10**3),
# (milli = 10**-3),
# (micro = 10**-6),
# (nano = 10**-9)
# ]
# ^^full variable has to be outside, in the list i only call the variable name
# but this one works:
# power = 10**9 
# print(power)
#   File "C:\SGL Developments\Systems Engineering\Week 1\prefix_converter.py", line 14
#     (giga = 10**9),
#      ^^^^^^^^^^^^
# SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
# base = input/select from prefixes (possible solution for loop)
# I'm close. solution is person inserts number, multiply by whatever prefix. Easy solution, pre-set unit e.g km to m
# But that is not practical. I need to give the person a choice of prefix

# print(5*kilo, "m")

# This code: (print is outside of for loop)

# giga = 10**9
# mega = 10**6
# kilo = 10**3
# milli = 10**-3
# micro = 10**-6
# nano = 10**-9

# prefixes = [giga, mega, kilo, milli, micro, nano]

# number = int(input("Enter number:"))
# for base in prefixes:
#     convert = number * base
# print(convert)

# only prints the last prefix = nano
# result = 5e-09

# Then this code (print inside for loop):

# giga = 10**9
# mega = 10**6
# kilo = 10**3
# milli = 10**-3
# micro = 10**-6
# nano = 10**-9

# prefixes = [giga, mega, kilo, milli, micro, nano]

# number = int(input("Enter number:"))
# for base in prefixes:
#     convert = number * base
#     print(convert)

# print all prefix conversions
# result:
# Enter number:5
# 5000000000
# 5000000
# 5000
# 0.005
# 4.9999999999999996e-06
# 5e-09

# this code:
# giga = 10**9
# mega = 10**6
# kilo = 10**3
# milli = 10**-3
# micro = 10**-6
# nano = 10**-9

# prefixes = [giga, mega, kilo, milli, micro, nano]

# number = int(input("Enter number:"))

# for index, item in enumerate(prefixes):
#     print(f"{index + 1}) {item}")

# while True:
#     try:
#         user_input = int(input("Enter the number of your choice:"))
        
#         if 1<= user_input <= len(prefixes):
#           base = prefixes[user_input-1]  
#           print(f"You selected:{base}")
#           break
#         else:
#             print("Invalid number: Try again")
#     except ValueError:
#         print("Please enter a valid option")

# base = prefixes
# convert = number * base
# print(convert)

# gives this result:
# Enter number:5
# 1) 1000000000
# 2) 1000000
# 3) 1000
# 4) 0.001
# 5) 1e-06
# 6) 1e-09
# Enter the number of your choice:3
# You selected:1000
# [1000000000, 1000000, 1000, 0.001, 1e-06, 1e-09, 1000000000, 1000000, 1, 1e-09, 1000000000, 1000000, 1000, 0.001, 1e-06, 1e-09, 1000000000, 101, 1e-06, 1e-09, 1000000000, 1000000, 1000, 0.001, 1e-06, 1e-09]

# this gives me a list of all the prefixes values

# the code with this:
# for base in prefixes:
#     convert = number * base
# print(convert)
# results in this:
# Enter number:5
# 1) 1000000000
# 2) 1000000
# 3) 1000
# 4) 0.001
# 5) 1e-06
# 6) 1e-09
# Enter the number of your choice:3 
# You selected:1000
# 5e-09
# this gives me the value of the last prefix. but for some reason the 5 still plays since it says 5e-09
# why?