radius = float(input("Enter in the radius of the circle: "))

pi = 3.14159265359

# this rounds to the nearest hundreths
area = round(pi*(radius**2), 2)

print "\nThe area of the circle with a radius of {x} is: {y}".format(y=area, x=radius)