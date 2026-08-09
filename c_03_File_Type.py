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
        elif response in ['integer', 'picture', 'int']:
            return "integer"

        # check for text...
        elif response in ['integer', 'int']:
            return "text"

        # if the response is invalid output an error
        else:
              print("Please enter a valid file type")


#Main routaine gose here
while True:
    file_type = get_filetype()
    print(f"you chose {file_type}")


    if file_type == "xxx":
        break


        