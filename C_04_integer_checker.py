# Ask user for width and loop until they
# enter a number that is more than zero
from P_04_get_wisth import width


def int_check(question, low):

    error = f"Please enter a number that is more than or equal to {low}\n"
    while True:

        try:
             # ask the user for a number
             response = float(input(question))

             # check that the number is more than zero

             if response >= low:
                 return response
             else:
                 print(error)

        except ValueError:
            print(error)

# Main Routine gose here
for item in range(0,  2):
    integer = int_check("integer: ", 0)
    print(integer)

print()

for item in range(0,  2):
    width = int_check("width: ", 1)
    print(width)

    print()
