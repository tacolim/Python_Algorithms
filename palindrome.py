"""
Return true if the given string is a palindrome. Otherwise, return false.

A palindrome is a word or sentence that's spelled the same way both forward and backward, ignoring punctuation, case, and spacing.

Note
You'll need to remove all non-alphanumeric characters (punctuation, spaces and symbols) and turn everything lower case in order to check for palindromes.

We'll pass strings with varying formats, such as "racecar", "RaceCar", and "race CAR" among others.

We'll also pass strings with special symbols, such as "2A3*3a2", "2A3 3a2", and "2_A3*3#A2".
"""

def palindrome(x):

    low = x.lower()
    low_o = low.replace(" ", "")
    low_ol = low_o.translate(None, ",.:;?!'\"'@#$%^&*()-_=+/><\\")
    back_low_ol = low_ol[::-1]


    if low_ol == back_low_ol:
        return True
    else:
        return False

print "racecar\n", palindrome("racecar"), "\n\n"
print "RaceCar\n", palindrome("RaceCar"), "\n\n"
print "race CAR\n", palindrome("race CAR"), "\n\n"
print "2A3*3a2\n", palindrome("2A3*3a2"), "\n\n"
print "2A3 3a2\n", palindrome("2A3 3a2"), "\n\n"
print "2_A3*3#A2\n", palindrome("2_A3*3#A2"), "\n\n"
print "Peter Piper picked a peck of pickled peppers. A peck of pickled peppers Peter Piper picked.\n", palindrome("Peter Piper picked a peck of pickled peppers. A peck of pickled peppers Peter Piper picked."), "\n\n"
print "A man, a plan, a canal: Panama.\n", palindrome("A man, a plan, a canal: Panama."), "\n\n"
print "Summit & summit & summit\n", palindrome("Summit & summit & summit"), "\n\n"
print "kayak\n", palindrome("kayak"), "\n\n"
