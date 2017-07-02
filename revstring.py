#make a function that reverses a string without using [::-1]

def reverse_string(x):
    print x, "\n\n"

    char = list(x)
    print char, "\n\n"

    rev_char = []

    lenchar = len(char)
    while lenchar != 0:
        rev_char.append(char.pop())
        lenchar -= 1

    print rev_char, "\n\n"

    revstring = ''.join(rev_char)

    return revstring

print reverse_string("Peter Piper picked a peck of pickled peppers.\n"
        "A peck of pickled peppers Peter Piper picked.\n"
        "If Peter Piper picked a peck of pickled peppers,\n"
        "where is the peck of pickled peppers Peter Piper picked?\n"
        "$120.39 for a peck of pickled peppers!")
