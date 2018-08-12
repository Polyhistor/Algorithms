# Version 1

letters = []

for i in 'human':
    letters.append(i)


print(letters)


# Version 2

letters_2 = [ i for i in 'human' ]

print(letters_2)


# Version 3

numbers = [ x for x in range(20) if x % 10 == 0 if x % 5 == 0]

print(numbers)

# Version 4

numbers = [ "eve" if x%2==0 else "odd" for x in range(10) ]

print(numbers)


