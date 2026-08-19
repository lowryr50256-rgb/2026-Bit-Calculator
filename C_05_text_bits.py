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


# Main Routine gose here
text_ans = calc_text_bits()
print(text_ans)