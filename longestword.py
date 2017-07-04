#Return the length of the longest word in the provided sentence. Your response should be a number.

def longestword(x):
    print "What is the length of the longest word in", "'"+x+"'", "?"
    words = x.split()
    lw = max(words, key=len)
    return len(lw)

print longestword("The quick brown fox jumped over the lazy dog."), "\n\n"
print longestword("Peter Piper picked a peck of pickled peppers."), "\n\n"
print longestword("To be or not to be? That is the question."), "\n\n"
print longestword("May the force be with you"), "\n\n"
print longestword("Google do a barrel roll"), "\n\n"
print longestword("What is the average airspeed velocity of an unladen swallow"), "\n\n"
print longestword("What if we try a super-long word such as otorhinolaryngology"), "\n\n"
