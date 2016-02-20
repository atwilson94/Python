# this exercise explains strings and text
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# this line inserts two variables into a string
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# these lines are printing with formatters. A string is put inside a string in these two lines
# %r is used for debugging
print "I said %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# this line tells python to print the joke_evaluation and also tells
# python that the formatter is a place holder for the variable "hilarious"
# which means "False" in this exercise
# another place where a string is put inside a string
print joke_evaluation % hilarious

# this is the left side of the string
w = "This is the left side of..."
# this is the right side of the string
e = "a string with a right side."

# the puts the two strings together with addition
print w + e