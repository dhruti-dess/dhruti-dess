# introduce project and part 1
print('Hello, welcome to my first project!')
print(' ' * 45)
print('This is part 1')
print(' ' * 45)

# ask their name
name = input('I am Dhruti. What is your name?:\n')
name = name.capitalize() # capitalize their name

# output their name
print('It is nice to meet you ' + name + '!')

# introduce questions
print('I have a few questions for you so I could get to know you a little better.')
print(' ' * 45)

# ask where they live
liveWhere = input('The first questions is, where do you live? (what town):\n')
liveWhere = liveWhere.capitalize()

# ask what they are majoring in
whatMajor = input('The next question is, what is your major?:\n')

# ask their favorite color
favoriteColor = input('The last question is, what is your favorite color?:\n')

# print all their information in separate lines
print('So ' + name + ', you live in ' + liveWhere + '.' + ' I love it there!')
print(' ' * 45)
print('You also said that you are majoring in ' + whatMajor + '.' + ' That is a very awesome choice!')
print(' ' * 45)
print('Lastly, you said your favorite color is ' + favoriteColor + '.' + ' That is such a good choice, my favorite color is light blue!')
print(' ' * 45)

# finish part 1
print('Well, it was very nice getting to know you ' + name + '.')
print(' ' * 45)
print('_' * 45)
print('_' * 45)

# introduce part 2
print(' ' * 45)
print('Welcome to part 2')
print(' ' * 45)
print('Hello! today I am going to tell you how many characters there are in your name!')

# ask their name
name = input('What is your name?:\n')
characters = len(name)

# tell them how many characters there are in their name
print(' ' * 45)
print('There are', characters,'characters in your name!')
#finish part 2
print(' ' * 45)
print('_' * 45)
print('_' * 45)
print(' ' * 45)

# introduce part 3
print('Welcome to part 3')
print(' ' * 45)

# define function
def print_total_inches(feet, inches):
    x = (feet*12) + inches
    return x

# introduce what we are doing
print('Hello, today we are going to convert feet and inches mixed measurements to inches using python!')
print(' ' * 45)
print('Please enter the following measurments:')
print(' ' * 45)
# ask for feet and inches that will be converted
feet = int(input('Enter a measurement in feet:'))
inches = int(input('Enter a measurement in inches:'))

# convert using function
convertedInches = print_total_inches(feet, inches)

# print answer
print(' ' * 45)
print('In inches the total is:', convertedInches, 'inches.')
# finish part 3print('_' * 15)
print(' ' * 45)
print('_' * 45)
print('_' * 45)
print(' ' * 45)
# introduce part 4
print('Welcome to part 4')
print(' ' * 45)
from datetime import datetime

# list all even numbers in time
even = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 
     42, 44, 46, 48, 50, 52, 54, 56, 58]

# give the minutes their own variable
time = datetime.today().minute

x = time

# true or false segment
if x in even:
    print('The current minute is', time, 'and it is even.')
else:
    print('The current minute is', time, 'and it is not even.')

# goodbye
print(' ' * 45)
print('This is the end of my first project! Goodbye!')
print(' ' * 45)
print('_' * 45)
print('_' * 45)
