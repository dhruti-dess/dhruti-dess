# A5 B1 C3 D4 E2

print('Welcome to Project 3')
print(' ')
print('-' * 60)
# question 2
print('\nQuestion 2:')

class Spiderman:
    def __init__(self, name, firstMovie, numberOfMovies, girlfriend):
        self.name = name
        self.firstMovie = firstMovie
        self.numberOfMovies = numberOfMovies
        self.girlfriend = girlfriend



spiderman1 = Spiderman('Tobey Maguire', 'Spiderman', 3, 'Mary Jane')

print('\nFirst actor that played Spiderman: ' + spiderman1.name)
print('His first movie\'s name in the series: ' + spiderman1.firstMovie)
print('Number of spiderman movies in his series: ', spiderman1.numberOfMovies)
print('The name of his girlfriend in the movies: ' + spiderman1.girlfriend)
print(' ')
print('-' * 60)
# question 3
print('\nQuestion 3:')
def wordCount(x):
    numWords = 0
    for string in x:
        words = string.split()
        numWords += len(words)
    return numWords
def findLongWord(x):
    longWord = ''
    for string in x:
        words = string.split()
        for word in words:
            if len(word) > len(longWord):
                longWord = word
    return longWord
def findAvgLen(x):
    totalLen = 0
    for string in x:
        words = string.split()
        for word in words:
            totalLen += len(word)
    avgWordLen = totalLen/numWords
    return avgWordLen
spidermanActors = ["Tobey", "Andrew", "Tom"]
numWords = wordCount(spidermanActors)
longWord = findLongWord(spidermanActors)
avgWordLen = findAvgLen(spidermanActors)
avgWordLen = round(avgWordLen, 1)
print('I will be finding the number of words, the longest word, \nand the average word length in this list:', spidermanActors)
print('\nThe number of words is:', numWords)
print('The longest word/name is:', longWord)
print('The average word length is:', avgWordLen)
print(' ')
print('-' * 60)
# question 4
print('\nQuestion 4:')

class PhonePlan:
    def __init__(self, num_mins = 0, num_messages = 0):
        self.num_mins = num_mins
        self.num_messages = num_messages
    def print_plan(self):
        print('Mins:', self.num_mins, end='')
        print(' Messages:', self.num_messages)

my_plan = PhonePlan(200, 300)
dads_plan = PhonePlan()
print('My plan...', end='')
my_plan.print_plan()
print('Dad\'s plan...', end='')
dads_plan.print_plan()

# end of Project 3
print(' ')
print('-' * 60)
