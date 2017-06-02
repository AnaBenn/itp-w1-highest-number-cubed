"""This is the entry point of the program."""

#mine
'''def highest_number_cubed(limit):
    cubed = 0
    for i in range(limit):
        if i**3 >= limit:
            cubed = i-1
            return(cubed)'''

#jason
def highest_number_cubed(limit):
    number = 0
    while True:
        number += 1
        if number**3 > limit:
            return(number - 1)
        