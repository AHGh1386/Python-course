my_string = "Hello, World!"

# String methods
print(my_string.upper())  # Output: HELLO, WORLD!
print(my_string.lower())  # Output: hello, world!
print(my_string.capitalize())  # Output: Hello, world!
print(my_string.title())  # Output: Hello, World!
print(my_string.swapcase())  # Output: hELLO, wORLD!
print(my_string.count("l"))  # Output: 3
print(my_string.startswith("Hello"))  # Output: True
print(my_string.endswith("World!"))  # Output: True
print(my_string.find("o"))  # Output: 4
print(my_string.rfind("o"))  # Output: 8
print(my_string.index("W"))  # Output: 7
print(my_string.rindex("o"))  # Output: 8
print(my_string.replace("o", "e"))  # Output: Helle, Werld!
print(my_string.strip())  # Output: Hello, World!
print(my_string.lstrip("H"))  # Output: ello, World!
print(my_string.rstrip("!"))  # Output: Hello, World
print(my_string.split(","))  # Output: ['Hello', ' World!']
print(my_string.split(" "))  # Output: ['Hello,', 'World!']
print(my_string.isalpha())  # Output: False
print(my_string.isdigit())  # Output: False
print(my_string.isalnum())  # Output: False
print(my_string.islower())  # Output: False
print(my_string.isupper())  # Output: False
print(my_string.isspace())  # Output: False
print(my_string.isnumeric())  # Output: False
print(my_string.isdecimal())  # Output: False
print(my_string.isprintable())  # Output: True
print(my_string.center(20, "*"))  # Output: ****Hello, World!****
print(my_string.zfill(20))  # Output: 0000000Hello, World!
print(my_string.encode())  # Output: b'Hello, World!'
print(my_string.endswith("world!"))  # Output: Fals
