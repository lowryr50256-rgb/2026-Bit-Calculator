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


# Main routine gose here
while True:
    file_type = get_filetype()

    # if user chose 'i',ask if they want an image / integer
    if file_type =='i':

        want_image = input("press <enter> for an integer or any other key for an image. ")

        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    print(f"you chose {file_type}")

    if file_type == "xxx":
        break




    print(f"you chose {file_type}")


    if file_type == "xxx":
        break


