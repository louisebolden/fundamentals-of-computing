import math
import random

###################################################
# Expressions
###################################################

# 1. There are 5280 feet in a mile. Write a Python statement that calculates and prints the number of feet in 13 miles.

print 5280 * 13

# 2. Write a Python statement that calculates and prints the number of seconds in 7 hours, 21 minutes and 37 seconds.

print (7 * 60 * 60) + (21 * 60) + 37

# 3. The perimeter of a rectangle is 2w+2h, where w and h are the lengths of its sides. Write a Python statement that calculates and prints the length in inches of the perimeter of a rectangle with sides of length 4 and 7 inches.

print (2 * 4) + (2* 7)

# 4. The area of a rectangle is wh, where w and h are the lengths of its sides. Note that the multiplication operation is not shown explicitly in this formula. This is standard practice in mathematics, but not in programming. Write a Python statement that calculates and prints the area in square inches of a rectangle with sides of length 4 and 7 inches.

print 4 * 7

# 5. The circumference of a circle is 2πr where r is the radius of the circle. Write a Python statement that calculates and prints the circumference in inches of a circle whose radius is 8 inches. Assume that the constant π=3.14.

print 2 * 3.14 * 8

# 6. The area of a circle is πr^2 where r is the radius of the circle. (The raised 2 in the formula is an exponent.) Write a Python statement that calculates and prints the area in square inches of a circle whose radius is 8 inches. Assume that the constant π=3.14.

print 3.14 * 8 ** 2

# 7. Given p dollars, the future value of this money when compounded yearly at a rate of r percent interest for y years is p(1+0.01r)^y. Write a Python statement that calculates and prints the value of 1000 dollars compounded at 7 percent interest for 10 years.

print 1000 * (1 + 0.01 * 7) ** 10

# 8. Write a single Python statement that combines the three strings "My name is", "Joe" and "Warren" (plus a couple of other small strings) into one larger string "My name is Joe Warren." and prints the result.

print "My name is " + "Joe" + " " + "Warren" + "."

# 9. Write a Python expression that combines the string "Joe Warren is 52 years old." from the string "Joe Warren" and the number 52 and then prints the result (Hint: Use the function str to convert the number into a string.)

print "Joe Warren" + " is " + str(52) + " years old."

# 10. The distance between two points (x0,y0) and (x1,y1) is √(x0−x1)^2+(y0−y1)^2. Write a Python statement that calculates and prints the distance between the points (2,2) and (5,6).

print ( ((2-5) ** 2) + (2-6) ** 2 ) ** 0.5

###################################################
# Variables and assignments
###################################################

# 1. Given a template that pre-defines a variable miles, write an assignment statement that defines a variable feet whose value is the number of feet in miles miles.

miles = 13
feet = miles * 5280

# 2. Given a template that pre-defines three variables hours, minutes and seconds, write an assignment statement that updates the variable total_seconds to have a value corresponding to the total number of seconds for hours hours, minutes minutes and seconds seconds.

hours = 7
minutes = 21
seconds = 37
total_seconds = (hours * 60 * 60) + (minutes * 60) + seconds

# 3. Given a template that pre-defines the variables width and height that are the lengths of the sides of a rectangle, write an assignment statement that defines a variable perimeter whose value is the perimeter of the rectangle in inches.

width = 4
height = 7
perimeter = (2 * width) + (2 * height)

# 4. Given a template that pre-defines the variables width and height that are the lengths of the sides of a rectangle, write an assignment statement that defines a variable area whose value is the area of the rectangle in square inches.

width = 4
height = 7
area = width * height

# 5. Given a template that pre-defines the constant PI and the variable radius corresponding to the radius of a circle in inches, write an assignment statement that defines a variable circumference whose value is the circumference of a circle with radius radius in inches.

PI = 3.14
radius = 8
circumference = 2 * PI * radius

# 6. Given a template that pre-defines the constant PI and the variable radius corresponding to the radius of a circle in inches, write an assignment statement that defines a variable area whose value is the area of a circle with radius radius in square inches.

PI = 3.14
radius = 8
area = PI * radius ** 2

# 7. Given the pre-defined variables present_value, annual_rate and years, write an assignment statement that define a variable future_value whose value is present_value dollars invested at annual_rate percent interest, compounded annually for years years.

present_value = 1000
annual_rate = 7
years = 10
future_value = present_value * (1 + 0.01 * annual_rate) ** years

# 8. Give the pre-defined variables first_name and last_name, write an assignment statement that defines the variable name_tag whose value is the string "My name is % %." where the percents should be replaced by first_name and last_name. Note that, in Python, you can use the + operator on strings to concatenate (i.e. join) them together into a single string.

first_name = "Joe"
last_name = "Warren"
name_tag = "My name is %s %s." % (first_name, last_name)

# 9. Given the pre-defined variables name (a string) and age (a number), write an assignment statement that defines a variable statement whose value is the string "% is % years old." where the percents should be replaced by name and the string form of age.

name = "Joe Warren"
age = 52
statement = name + " is " + str(age) + " years old."

# 10. Given the variables x0, y0, x1, and y1, write an assignment statement that defines a variable distance whose values is the distance between the points (x0,y0) and (x1,y1).

x0 = 2
y0 = 2
x1 = 5
y1 = 6
distance = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5

# 11. Challenge: Heron's formula states the area of a triangle is √s(s−a)(s−b)(s−c) where a, b and c are the lengths of the sides of the triangle and s=1/2(a+b+c) is the semi-perimeter of the triangle. Given the variables x0, y0, x1,y1, x2, and y2, write a Python program that computes a variable area whose value is the area of the triangle with vertices (x0,y0), (x1,y1) and (x2,y2). (Hint: our solution uses five assignment statements.)

x0, y0 = 0, 0
x1, y1 = 3, 4
x2, y2 = 1, 1
a = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
b = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
c = ((x0 - x2) ** 2 + (y0 - y2) ** 2) ** 0.5
s = 0.5 * (a + b + c)
area = ( s * (s - a) * (s - b) * (s - c) ) ** 0.5

###################################################
# Functions
###################################################

# 1. Write a Python function miles_to_feet that takes a parameter miles and returns the number of feet in miles miles.

def miles_to_feet(miles):
  return miles * 5280

# 2. Write a Python function total_seconds that takes three parameters hours, minutes and seconds and returns the total number of seconds for hours hours, minutes minutes and seconds seconds.
# (Note: _fn suffix added because total_seconds was already defined above)

def total_seconds_fn(hours, minutes, seconds):
  return (hours * 60 * 60) + (minutes * 60) + seconds

# 3. Write a Python function rectangle_perimeter that takes two parameters width and height corresponding to the lengths of the sides of a rectangle and returns the perimeter of the rectangle in inches.

def rectangle_perimeter(width, height):
  return 2 * width + 2 * height

# 4. Write a Python function rectangle_area that takes two parameters width and height corresponding to the lengths of the sides of a rectangle and returns the area of the rectangle in square inches.

def rectangle_area(width, height):
  return width * height

# 5. Write a Python function circle_circumference that takes a single parameter radius corresponding to the radius of a circle in inches and returns the the circumference of a circle with radius radius in inches. Do not use π=3.14, instead use the math module to supply a higher-precision approximation to π.

def circle_circumference(radius):
  return 2 * math.pi * radius

# 6. Write a Python function circle_area that takes a single parameter radius corresponding to the radius of a circle in inches and returns the the area of a circle with radius radius in square inches. Do not use π=3.14, instead use the math module to supply a higher-precision approximation to π.

def circle_area(radius):
  return math.pi * radius ** 2

# 7. Write a Python function future_value that takes three parameters present_value, annual_rate and years and returns the future value of present_value dollars invested at annual_rate percent interest, compounded annually for years years.
# (Note: _fn suffix added because future_value was already defined above)

def future_value_fn(present_value, annual_rate, years):
  return present_value * (1 + 0.01 * annual_rate) ** years

# 8. Write a Python function name_tag that takes as input the parameters first_name and last_name (strings) and returns a string of the form "My name is % %." where the percents are the strings first_name and last_name. Reference the test cases in the provided template for an exact description of the format of the returned string.
# (Note: _fn suffix added because name_tag was already defined above)

def name_tag_fn(first_name, last_name):
  return "My name is " + first_name + " " + last_name + "."

# 9. Write a Python function name_and_age that takes as input the parameters name (a string) and age (a number) and returns a string of the form "% is % years old." where the percents are the string forms of name and age. Reference the test cases in the provided template for an exact description of the format of the returned string.

def name_and_age(name, age):
	return name + " is " + str(age) + " years old."

# 10. Write a Python function point_distance that takes as the parameters x0, y0, x1 and y1, and returns the distance between the points (x0,y0) and (x1,y1).

def point_distance(x0, y0, x1, y1):
  return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5

# 11. Challenge: Write a Python function triangle_area that takes the parameters x0, y0, x1, y1, x2, and y2, and returns the area of the triangle with vertices (x0,y0), (x1,y1) and (x2,y2). (Hint: use the function point_distance as a helper function and apply Heron's formula.)

def triangle_area(x0, y0, x1, y1, x2, y2):
  # calculate length of sides
  a = point_distance(x0, y0, x1, y1)
  b = point_distance(x0, y0, x2, y2)
  c = point_distance(x1, y1, x2, y2)
  # calculate semi-perimeter
  s = 0.5 * (a + b + c)
  return ( s * (s - a) * (s - b) * (s - c) ) ** 0.5

# 12. Challenge: Write a Python function print_digits that takes an integer number in the range [0,100), i.e., at least 0, but less than 100. It prints the message "The tens digit is %, and the ones digit is %.", where the percent signs should be replaced with the appropriate values. (Hint: Use the arithmetic operators for integer division // and remainder % to find the two digits. Note that this function should print the desired message, rather than returning it as a string.

def print_digits(number):
  print "The tens digit is " + str(number // 10) + ",",
  print "and the ones digit is " + str(number % 10) + "."

# 13. Challenge: Powerball is lottery game in which 6 numbers are drawn at random. Players can purchase a lottery ticket with a specific number combination and, if the number on the ticket matches the numbers generated in a random drawing, the player wins a massive jackpot. Write a Python function powerball that takes no arguments and prints the message "Today's numbers are %, %, %, %, and %. The Powerball number is %.". The first five numbers should be random integers in the range [1,60), i.e., at least 1, but less than 60. In reality, these five numbers must all be distinct, but for this problem, we will allow duplicates. The Powerball number is a random integer in the range [1,36), i.e., at least 1 but less than 36. Use the random module and the function random.randrange to generate the appropriate random numbers.Note that this function should print the desired message, rather than returning it as a string.

def powerball():
    print "Today's numbers are " + str(random.randrange(1, 60)) + ",",
    print str(random.randrange(1, 60)) + ",",
    print str(random.randrange(1, 60)) + ",",
    print str(random.randrange(1, 60)) + ", and",
    print str(random.randrange(1, 60)) + ". The Powerball number is",
    print str(random.randrange(1, 36)) + "."

###################################################
# Logic and conditionals
###################################################

# 1. Write a Python function is_even that takes as input the parameter number (an integer) and returns True if number is even and False if number is odd. Hint: Apply the remainder operator to n (i.e., number % 2) and compare to zero.

def is_even(number):
  return number % 2 == 0

# 2. Write a Python function is_cool that takes as input the string name and returns True if name is either "Joe", "John" or "Stephen" and returns False otherwise.

def is_cool(name):
  return (name == "Joe") or (name == "John") or (name == "Stephen")

# 3. Write a Python function is_lunchtime that takes as input the parameters hour (an integer in the range [1,12]) and is_am (a Boolean “flag” that represents whether the hour is before noon). The function should return True when the input corresponds to 11am or 12pm (noon) and False otherwise. If the problem specification is unclear, look at the test cases in the provided template. Our solution does not use conditional statements.

def is_lunchtime(hour, is_am):
	return (hour == 11 and is_am) or (hour == 12 and not is_am)

# 4. Write a Python function is_leap_year that take as input the parameter year and returns True if year (an integer) is a leap year according to the Gregorian calendar and False otherwise. The Wikipedia entry for leap yearscontains a simple algorithmic rule for determining whether a year is a leap year. Your main task will be to translate this rule into Python.

def is_leap_year(year):
	return ((year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0))

# 5. Write a Python function interval_intersect that takes parameters a, b, c, and d and returns True if the intervals [a,b] and [c,d] intersect and False otherwise. While this test may seem tricky, the solution is actually very simple and consists of one line of Python code. (You may assume that a≤b and c≤d.)

def interval_intersect(a, b, c, d):
    return (c <= b) and (a <= d)

# 6. Write a Python function name_and_age that take as input the parameters name (a string) and age (a number) and returns a string of the form "% is % years old." where the percents are the string forms of name and age. The function should include an error check for the case when age is less than zero. In this case, the function should return the string "Error: Invalid age".
# (Note: _2 suffix added because name_and_age was already defined above)

def name_and_age_2(name, age):
	if age >= 0:
		return name + " is " + str(age) + " years old."
	else:
		return "Error: Invalid age"

# 7. Write a Python function print_digits that takes an integer number in the range [0,100) and prints the message "The tens digit is %, and the ones digit is %." where the percents should be replaced with the appropriate values. The function should include an error check for the case when number is negative or greater than or equal to 100. In those cases, the function should instead print "Error: Input is not a two-digit number.".
# (Note: _2 suffix added because print_digits was already defined above)

def print_digits_2(number):
	if 0 <= number < 100:
		print "The tens digit is " + str(number // 10) + ",",
		print "and the ones digit is " + str(number % 10) + "."
	else:
		print "Error: Input is not a two-digit number."

# 8. Write a Python function name_lookup that takes a string first_name that corresponds to one of ("Joe", "Scott", "John" or "Stephen") and then returns their corresponding last name ("Warren", "Rixner", "Greiner" or "Wong"). If first_name doesn't match any of those strings, return the string "Error: Not an instructor".

def name_lookup(first_name):
	if first_name == "Joe":
		return "Warren"
	elif first_name == "Scott":
		return "Rixner"
	elif first_name == "John":
		return "Greiner"
	elif first_name == "Stephen":
		return "Wong"
	else:
		return "Error: Not an instructor"

# 9. Pig Latin is a language game that involves altering words via a simple set of rules. Write a Python function pig_latin that takes a string word and applies the following rules to generate a new word in Pig Latin. If the first letter in word is a consonant, append the consonant plus "ay" to the end of the remainder of the word. For example, pig_latin("pig") would return "igpay". If the first letter in word is a vowel, append "way" to the end of the word. For example, pig_latin("owl") returns "owlway". You can assume that word is in lower case. The provided template includes code to extract the first letter and the rest of word in Python. Note that, in full Pig Latin, the leading consonant cluster is moved to the end of the word. However, we don't know enough Python to implement full Pig Latin just yet.

def pig_latin(word):
	first_letter = word[0]
	rest_of_word = word[1:]

	if (first_letter == "a" or first_letter == "e" or first_letter == "i" or
	    first_letter == "o" or first_letter == "u"):
		return word + "way"
	else:
		return rest_of_word + first_letter + "ay"

# 10. Challenge: Given numbers a, b, and c, the quadratic equation ax^2+bx+c=0 can have zero, one or two real solutions (i.e; values for x that satisfy the equation). The quadratic formula x=(−b±√b^2−4ac)/2a can be used to compute these solutions. The expression b^2−4ac is the discriminant associated with the equation. If the discriminant is positive, the equation has two solutions. If the discriminant is zero, the equation has one solution. Finally, if the discriminant is negative, the equation has no solutions. Write a Python function smaller_root that takes an input the numbers a, b and c and returns the smaller solution to this equation if one exists. If the equation has no real solution, print the message "Error: No real solutions" and simply return. Note that, in this case, the function will actually return the special Python value None.
def smaller_root(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    # secret not mentioned: if a is zero, there are no solutions
    if discriminant < 0 or a == 0:
      print "Error: No real solutions"
    else:
      discriminant_sqrt = discriminant ** 0.5
      # Choose the positive or negative square root that leads to a smaller root
      if a > 0:
          smaller = -discriminant_sqrt
      else:
          smaller = discriminant_sqrt
      return (-b + smaller) / (2 * a)

###################################################
# Interactive applications
###################################################

# 1.

# 2.

# 3.

# 4.

# 5.

# 6.

# 7.

# 8.

# 9.

# 10.

###################################################
# Buttons and input fields
###################################################

# 1.

# 2.

# 3.

# 4.

# 5.

# 6.

# 7.

# 8.

# 9.

# 10.

###################################################
# Drawing
###################################################

# 1.

# 2.

# 3.

# 4.

# 5.

# 6.

# 7.

# 8.

# 9.

# 10.

###################################################
# Timers
###################################################

# 1.

# 2.

# 3.

# 4.

# 5.

# 6.

# 7.

# 8.

# 9.

# 10.

###################################################
# Lists
###################################################

# 1.

# 2.

# 3.

# 4.

# 5.

# 6.

# 7.

# 8.

# 9.

# 10.

###################################################
# Keyboard
###################################################

# 1.

# 2.

# 3.

# 4.

# 5.

# 6.

# 7.

# 8.

# 9.

# 10.

###################################################
# Mouse and list methods
###################################################

# 1.

# 2.

# 3.

# 4.

# 5.

# 6.

# 7.

# 8.

# 9.

# 10.

###################################################
# Dictionaries and images
###################################################

# 1.

# 2.

# 3.

# 4.

# 5.

# 6.

# 7.

# 8.

# 9.

# 10.

###################################################
# Classes pt 1
###################################################

# 1.

# 2.

# 3.

# 4.

# 5.

# 6.

# 7.

# 8.

# 9.

# 10.

###################################################
# Classes pt 2
###################################################

# 1.

# 2.

# 3.

# 4.

# 5.

# 6.

# 7.

# 8.

# 9.

# 10.

###################################################
# Sprites and sound
###################################################

# 1.

# 2.

# 3.

# 4.

# 5.

# 6.

# 7.

# 8.

# 9.

# 10.

###################################################
# Sets and collisions
###################################################

# 1.

# 2.

# 3.

# 4.

# 5.

# 6.

# 7.

# 8.

# 9.

# 10.
