giga = 10**9
mega = 10**6
kilo = 10**3
milli = 10**-3
micro = 10**-6
nano = 10**-9

prefixes = [giga, mega, kilo, milli, micro, nano]

number = int(input("Enter number:"))

for index, item in enumerate(prefixes):
    print(f"{index + 1}) {item}")

while True:
    try:
        user_input = int(input("Enter the number of your choice:"))
        
        if 1<= user_input <= len(prefixes):
          base = prefixes[user_input-1]  
          print(f"You selected:{base}")
          break
        else:
            print("Invalid number: Try again")
    except ValueError:
        print("Please enter a valid option")

for base in prefixes:
    convert = number * base
print(convert)