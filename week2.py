# Week 2 - Functions

name = str(input("Enter first & last name separated by single space: "))

space = name.find(" ")
first_name = name[:space].capitalize()
last_name = name[space + 1:].capitalize()

print(f"Hi {first_name} {last_name}")


