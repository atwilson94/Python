# this exercise covers variables and names
# this line lets python know "cars" has a number value of 100
cars = 100
# this line lets python know that the space in a car is equal to 4.0
# the "_" is called an underscore
space_in_a_car = 4
# this line lets python know "drivers" has a number value of 30
drivers = 30
# same as above but the variable is "passengers" and the value is 90
passengers = 90
# this line is subtracting drivers from cars and using that value to represent "cars_not_driven"
cars_not_driven = cars - drivers
# this line is a variable with a value representing another variable
cars_driven = drivers
# this line is multiplying variables with values to get a result for this particular variable
carpool_capacity = cars_driven * space_in_a_car
# this line is dividing two variables to represent a value for the particular variable
average_passengers_per_car = passengers / cars_driven


# these lines are combining the "print" function with math and variables
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."