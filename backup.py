
# Returns XOR of 'a' and 'b'
# (both of same length)
import random


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

        if random.uniform(0, 1) > 0.5:
            temp = '0'
        else:
            temp = '1'


        if j == 0 or j == k - 1:
            temp = '1'
        # Concatenation the random 0, 1
        # to the final result
        key += temp
    #print(key)
    return key


d = int(random_message(20), 2)
p = int('110101', 2)

print(bin(d)[2:])
print(bin(p)[2:])

k = len(bin(d)) - 2
n = len(bin(p)) + k - 3

d = d << (n - k)  # 2^(n-k)D

print("D: " + bin(d))

fcs = int(mod2div(bin(d)[2:], bin(p)[2:]), 2)

print("FCS: " + bin(fcs))

T = d + fcs

print("T: " + bin(T))

r1 = int(mod2div(bin(T)[2:], bin(p)[2:]), 2)

print("R: " + bin(r1))

