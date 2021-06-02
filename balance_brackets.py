import math

# Bank of opening and closing brackets
openers = ['(','[','{']
closers = [')',']','}']

def isBalanced(s):
    if s == '':
        return True
    elif s[0] in closers:
        return False
    elif s[0] in openers:
        if   s[1]  in closers and openers.index(s[0]) == closers.index(s[1]):
            return isBalanced(s[2:])
        elif s[-1] in closers and openers.index(s[0]) == closers.index(s[-1]):
            return isBalanced(s[1:-1])
    return False

# Tests first for empty string True condition
# Then tests for out-of-place right-hand brackets
# If the string/substring opens with an opening bracket...
# String is recursively tested if it immediately closes encapsulating an empty substring, or...
#   ...if the bracket pair encapsulates the rest of the string/substring.
# False is returned for the fallback situation unpaired open initial bracket.


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printString(string):
    print('[\"', string, '\"]', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    s1 = "{[(])}"
    expected_1 = False
    output_1 = isBalanced(s1)
    check(expected_1, output_1)

    s2 = "{{[[(())]]}}"
    expected_2 = True
    output_2 = isBalanced(s2)
    check(expected_2, output_2)

    # Add your own test cases here
    s3 = "{[()]}"
    expected_3 = True
    output_3 = isBalanced(s3)
    check(expected_3, output_3)

    s4 = "{}()"
    expected_4 = True
    output_4 = isBalanced(s4)
    check(expected_4, output_4)

    s5 = "{(})"
    expected_5 = False
    output_5 = isBalanced(s5)
    check(expected_5, output_5)

    s6 = ")"
    expected_6 = False
    output_6 = isBalanced(s6)
    check(expected_6, output_6)

