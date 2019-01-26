print("Hi! Welcome to my first Python01")

name = input("What is your name? ")
name = name.title().strip()
print(f"Hello {name}")

age = input("How old are you? ")
additional_year = 3
next_years = int(age) + additional_year

print(
    f"In next {additional_year} years, "
    f"you will {next_years} years old."
)

input()