print "You can only take one friend with you to spring break. \nDo you choose friend 1 or 2?"

friend = raw_input("> ")

if friend == "1":
	print "You both get wasted and your friend disappears. What do you do?"
	print "1. Call the Police."
	print "2. Look by yourself."
	
	choice = raw_input("> ")
	
	if choice == "1":
		print "You get arrested for public intoxication. Good going!"
	elif choice == "2":
		print "You found you friend!"
	else:
		print "Really? %s is your answer? Way to ruin the game!" % choice
		
elif friend == "2":
	print "Your vacation choices are:"
	print "1. Japan."
	print "2. Dubai."
	print "3. Your house."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "You and your friend come into a lot of money. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"
	
else:
	print "You missed your entire spring break to illness. Bummer!"