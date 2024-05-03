# postfix.py
# Aidan Nachi
# 2024.31.3
#
# This file converts infix expressions into
# postfix expressions.
#
# This file defines a convert_to_postfix function that rearranges
# the values in an infix expression to a postfix expression that is
# outputted for users to see. It also features a precedence function
# that assists in this process. The file has two functions to handle file
# and user input and prints output posftix expressions.


from stack import Peek_stack

# CONSTANT VALUES
# Sets maximum value of inputted values in the storage.
# (Would only be used if we used the Array_stack)
# STORAGE_STACK_SIZE = 40


def precedence(operator):
    """ Establish precedence of operators. """

    # When comparing precedence of operators, refer to these
    # numbers that give a precedence level for operators.
    precedence_level = 0

    if operator == '+' or operator == '-':
        precedence_level = 1

    elif operator == '*' or operator == '/':
        precedence_level = 2

    elif operator == '^':
        precedence_level = 3

    return precedence_level


def convert_to_postfix(infix_expression):
    """ Convert the infix expression to postfix. """

    # Example, infix_expression = 2+3*5-2
    #
    # Pass 1: Input 2 in postfix.
    # postfix_expression = 2, storage = []
    #
    # Pass 2: Push + onto storage.
    # postfix_expression = 2, storage = [+]
    #
    # Pass 3: Input 3 in postfix.
    # postfix_expression = 23, storage = [+]
    #
    # Pass 4: Push * onto storage.
    # postfix_expression = 23, storage = [+, *]
    #
    # Pass 5: Input 5 in postfix.
    # postfix_expression = 235, storage = [+, *]
    #
    # Pass 6: Pop + and * into postfix and push - onto stack.
    # postfix_expression = 235*+, storage = [-]
    #
    # Pass 7: Input 2 in postfix.
    # postfix_expression = 235*+2, storage = [-]
    #
    # Pass 8: Empty the storage by popping - into postfix.
    # postfix_expression = 235*+2-, storage = []

    # We will be adding values into a string that resemble a postfix
    # expression.
    postfix_expression = ''

    # We will be setting non-digit values aside so we can add them to
    # the postfix expression later.
    storage_stack = Peek_stack()

    for sym in infix_expression:

        # We want digits to be inputted into the postfix expression.
        if sym in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            postfix_expression += sym

        # Operators will be moved into storage to be saved until another
        # operator of lower precedence forces them into the postfix expression.
        elif sym in ['+', '-', '*', '/', '^'] and storage_stack.is_empty():
            storage_stack.push(sym)

        # Use the open parenthesis as a boundary in storage for all of the low
        # precedence operators inside the infix expression parenthesis until a closing
        # parenthesis forces them onto the postfix expression.
        elif sym == '(':
            storage_stack.push(sym)

        # High precedence operators get added to the postfix expression while ones with
        # lower precedence get put it storage.
        elif sym in ['+', '-', '*', '/']:
            while not storage_stack.is_empty() \
                and precedence(sym) <= precedence(storage_stack.peek_stack_value()):

                postfix_expression += storage_stack.pop()

            storage_stack.push(sym)

        # Skip past spaces in the infix expressions to the next value.
        elif sym == ' ':
            pass

        # Operators with right associativity are prioritized for postfix expressions.
        elif sym == '^':
            storage_stack.push(sym)

        # Input operators inbetween the parenthesis in order of their precedence
        # (high to low) into the postfix expression.
        elif sym == ')':
            while storage_stack.peek_stack_value() != '(':
                postfix_expression += storage_stack.pop()
            storage_stack.pop()

    # Input remaining operators in the stack into our postfix expression
    # form the top down.
    while not storage_stack.is_empty():
        postfix_expression += storage_stack.pop()

    return postfix_expression


def do_user_input():
    """ Turn user input infix expression to postfix. """

    # Title and description for user to read.
    print("\nPOSTFIX CONVERTER\n")
    print("The Postfix Converter converts inputted infix expressions to postfix.\n")

    # Directions and rules for user to follow.
    print("\nDirections: Enter an valid infix expression according to the rules below",
           "and press the return key.")

    print("\nRules: \n")
    print("1. You can only enter single digit numbers that range from 0-9")
    print("2. You may only enter binanry operators including: +, -, *, /, ^")
    print("3. Each open parenthesis must be closed with a close parenthesis")
    print("4. Each operator must be followed by a number and vice versa")
    print("5. You can only enter up to 50 characters max. \n")

    # Allow user to input infix expressions as many times as they like.
    while True:
        print("ENTER 'stop' TO EXIT")
        user_infix_input = input("Enter an infix expression: ")

        if user_infix_input == 'stop':
            print(" ")
            break

        # Seperate the output for the user input for users to easily view.
        else:
            print("\n----------------------------------------------------------"+
                  "------------------------------------------------------------")
            print(f"Infix Expression: {user_infix_input}\n")

            output_postfix = convert_to_postfix(user_infix_input)

            print(f"Postfix Expression: {output_postfix}")
            print("------------------------------------------------------------"+
                  "----------------------------------------------------------\n")


def do_file_input():
    """ Turn file of infix expressions to postfix. """

    # Give users the option to submit a file to convert to postfix.
    user_file_option = input("Do you want to enter a test file (y/n): ")

    if user_file_option == 'y':
        file_input = input("Name of test file: ")

        with open(file_input) as f:
            for line in f:

                # Clean up line to read and convert.
                line = line.rstrip('\n')
                is_empty_str = (len(line.strip())==0)

                # Check to see if the line is empty or a comment.
                if not is_empty_str and line[0] == '#':
                    continue

                # Display the file contents converted to postfix.
                output_postfix = convert_to_postfix(line)
                print(output_postfix)
            print('')

    elif user_file_option == 'n':
        print(" ")

def main():
    """ Demonstrate postfix conversion functionality. """

    do_user_input()
    do_file_input()

if __name__ == "__main__":
    main()

