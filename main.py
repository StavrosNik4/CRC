# importing libraries
import random
import numpy

"""
Source for the next 2 functions (xor and modulo2)
https://www.geeksforgeeks.org/modulo-2-binary-division/
"""


# Returns XOR of 'a' and 'b'
# (both of same length)
def xor(a, b):
    # initialize result
    result = []
    # Traverse all bits, if bits are
    # same, then XOR is 0, else 1
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)


# Performs Modulo-2 division
def mod2div(dividend, divisor):
    # Number of bits to be XORed at a time.
    pick = len(divisor)

    # Slicing the dividend to appropriate
    # length for particular step
    tmp = dividend[0: pick]

    while pick < len(dividend):

        if tmp[0] == '1':

            # replace the dividend by the result
            # of XOR and pull 1 bit down
            tmp = xor(divisor, tmp) + dividend[pick]

        else:  # If leftmost bit is '0'
            # If the leftmost bit of the dividend (or the
            # part used in each step) is 0, the step cannot
            # use the regular divisor; we need to use an
            # all-0s divisor.
            tmp = xor('0' * pick, tmp) + dividend[pick]

        # increment pick to move further
        pick += 1

    # For the last n bits, we have to carry it out
    # normally as increased value of pick will cause
    # Index Out of Bounds.
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    checkword = tmp
    return checkword


# Function to create the
# random binary string
def random_message(k):
    # Variable to store the
    # string
    key = ""

    # Loop to find the string
    # of desired length
    for j in range(k):
        # randint function to generate
        # 0, 1 randomly and converting
        # the result into str
        temp = str(random.getrandbits(1))

        if j == 0 or j == k - 1:
            temp = '1'
        # Concatenation the random 0, 1
        # to the final result
        key += temp
    return key


# function that may change the message
# according to the Bit Error Rate (ber)
def error(mes, ber):
    temp_list = list(mes)
    for v in range(0, len(mes)):
        ran = numpy.random.uniform(0, 1)
        if ran < ber:  # if random number < Bit Error Rate: an error has occurred
            if temp_list[v] == '0':
                temp_list[v] = '1'
            else:
                temp_list[v] = '0'

    temp1 = "".join(temp_list)
    return temp1


"""
Main Code
"""

# User input
num_messages = int(input("Give number of messages: "))
k = int(input("Give size of each message (k): "))
P = input("Give P (binary): ")
BER = float(input("Give BER (0-1): "))

n = len(P) + k - 1

# error counters initialization
errors1 = 0  # errors by bit error rate
errors2 = 0  # errors noticed by CRC

# Loop for each message
for i in range(0, num_messages):

    message = random_message(k)                 # Creating random message
    message = message + (n - k) * "0"           # Shifting the random message (n-k) bits to the left
    fcs = mod2div(message, P)                   # Calculating its FCS
    t = bin(int(message, 2) + int(fcs, 2))[2:]  # Creating the T messages

    # Bit Error Rate / Transmission Media
    tmp = error(t, BER)
    if int(tmp, 2) != int(t, 2):
        t = tmp
        errors1 = errors1 + 1

    # Receiver
    if int(mod2div(t, P), 2) != 0:
        errors2 = errors2 + 1


# printing the results
print("Errors by Bit Error Rate: " + str(errors1 / num_messages * 100)[:9] + " %")
if errors1 != 0:
    x = errors2 / errors1 * 100
    print("Errors found by CRC (over errors): " + str(x)[:9] + " %")
    y = (errors1 - errors2) / errors1 * 100
    print("Errors not found by CRC (over errors): " + str(y)[:9] + " %")
    x = errors2 / num_messages * 100
    print("Errors found by CRC (over total messages): " + str(x)[:9] + " %")
    y = (errors1 - errors2) / num_messages * 100
    print("Errors not found by CRC (over total messages): " + str(y)[:9] + " %")
print("errors by ber (errors1): " + str(errors1))
print("errors found by crc (errors2): " + str(errors2))
print("errors not found by crc: " + str(errors1 - errors2))

