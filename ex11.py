print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

# Use %s to show just what you typed. %r is for debugging
print "So, you're %s old, %s tall, and %s heavy." % (
age, height, weight)