# Generates headings (eg: ---- Heading ----) 1 usage
def statement_generator (statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
 Instructions go here.
- instructions 1
- instructions 2
- etc
    ''')


# Ask user for width and loop until they
# enter a number that is more than zero


def int_check(question, low):

    error = f"Please enter a number that is more than or equal to {low}\n"
    while True:

        try:
             # ask the user for a number
             response = int(input(question))

             # check that the number is more than zero

             if response >= low:
                 return response
             else:
                 print(error)

        except ValueError:
            print(error)



# calculates how many bits are needed to represent an integer
def image_calc():
    pass
    width = int_check("width: ", 1)
    height = int_check("height: ", 1)

    # calculate the number of pixles and multiply by 24 to get the number of bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    # set up answer and return it
    answer = (f"Number of pixels: {width} x {height} = {num_pixels}"
              f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")

    return answer


# asks users for file type (integer / image / text / xxx) 1 usage
def get_filetype():


           while True:
                response = input("File type: ").lower()

                # check  for 'i' or the exit code
                if response == "xxx" or response == "i":
                    return response

                # check if it's an integer
                elif response in ['integer', 'int']:
                    return "integer"

                # check for an image...
                elif response in ['image', 'picture', 'int', 'p']:
                    return "image"

                # check for text...
                elif response in ['text ', 'txt', 't']:
                    return "text"

                # if the response is invalid output an error
                else:
                      print("Please enter a valid file type")

# calculates how many bits are needed to represent an integer
def integer_calc():
    # Ask the user to enter an interger (more than / equal to 0)
    integer = int_check("Integer: ",  0)

    # convert the interger to binary and work out the number of bits needed
    raw_binary = bin(integer)

    # remove the leading  '0b' from the raw binary conversion
    binary = raw_binary[2:]
    num_bits = len(binary)


    # Set up answer and return it
    answer =f"{integer} in binary is {binary}. we ned {num_bits} to represent it."

    return answer

# Calculates number of bits needed to represent text in ascii
def calc_text_bits():

    # Get text from user
    resource = input("Enter some text...")

    # Calculate bits needed
    num_chars = len(resource)
    num_bits = num_chars * 8

    # Set up answer and return it
    answer = (f"{resource} has {num_chars} characters."
              f"\nWe need {num_chars} x 8 bits to represent it"
              f"\nwhich is {num_bits} bits")

    return answer


# Main routine gose here

 # Ask user for width and loop until they
# enter a number that is more than zero

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                           "or any key to continue ")

if want_instructions == "":
    instructions()


while True:
    file_type = get_filetype()

    if file_type == "xxx":
        break

    # if user chose 'i',ask if they want an image / integer
    if file_type =='i':

        want_image = input("press <enter> for an integer or any other key for an image. ")

        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image:"

    if file_type == "image":
        image_ans = image_calc()
        print(image_ans)
    elif file_type == "integer":
        integer_ans = integer_calc()
        print(integer_ans)
    else:
        text_ans = calc_text_bits()
        print(text_ans)





