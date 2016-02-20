name = 'Aaron T. Wilson'
age = 21
height = 69
weight = 190
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pound heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth


print "If I add %d, %d, and %d I get %d." % (
age, height, weight, age + height + weight)
# %r, %d, %s are all formatters that tell python what to do.