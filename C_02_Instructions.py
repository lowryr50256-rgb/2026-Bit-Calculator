# Generates headings (eg: ---- Heading ----) 1 usage
def statement_generator (statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")


# Main routine goes here
want_instructions = input("Press <enter> to read the instructions "
                           "or any key to continue ")

if want_instructions == "":
    instructions()

print("program continues")
