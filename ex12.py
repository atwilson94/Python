# this is another way to get someone to give raw input.
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

# remember that %r is for debugging, so use %s instead.
print "So, you're %s old, %s tall, and %s heavy." % (
age, height, weight)