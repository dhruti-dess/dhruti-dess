print('Welcome to project 2') # introduce project 2
print('We will be doing 4 programs based on Ken Griffey Jr. career by season')

print(' ' * 45)
print(' ' * 45)
print('_' * 45)
print(' ' * 45)
# these are the lists

gamesPlayed = [127, 155, 154, 142, 156, 111, 72, 140, 157, 161, 160, 145,
               111, 70, 53, 83, 128, 109, 144, 143, 117,  33]
plateAppearances = [506,666,633,617,691,493,314,639,704,720,706,631,417,
                    232,201,348,555,472,623,575,454,108]
atBats = [455,597,548,565,582,433,260,545,608,633,606,520,364,197,166,300,
          491,428,528,490,387,98]
hits = [120,179,179,174,180,140,67,165,185,180,173,141,104,52,41,76,148,108,146,122,83,18]
strikeouts = [83,81,82,67,91,73,53,104,121,121,108,117,72,39,44,67,93,78,99,
             89,80,17]

# program 1: calculate batting average
print('\nProgram 1: Calculating Ken Griffey Jr. Batting Average for his entire career')

battingAverage = sum(hits)/sum(atBats)
battingAverage = round(battingAverage, 3)
print('\nKen Griffey Jr. Batting Average: ', battingAverage)

print(' ' * 45)
print('_' * 45)
print(' ' * 45)
print('_' * 45)
print(' ' * 45)

# program 2: calculate batting average
print('\nProgram 2: Calculating Ken Griffey Jr. Strikeout Percentage for his entire career')

for x in range(len(strikeouts)):
    strikeoutPercentage = strikeouts[x] / plateAppearances[x]
    strikeoutPercentage = (strikeoutPercentage * 100)
    strikeoutPercentage = round(strikeoutPercentage, 1)
    print(f'\nKen Griffey Jr. Strikeout Percentage for season {x+1}: ', strikeoutPercentage, "%")

print(' ' * 45)
print('_' * 45)
print(' ' * 45)
print('_' * 45)
print(' ' * 45)

# program 3: list 3 lowest total in At-Bats
print('\nProgram 3: List of Ken Griffey Jr. 3 lowest total in At-Bats for his entire career')

sortedAtBats = sorted(atBats)
lowestTotalAtBats = sortedAtBats[:3]
print('\nList of Ken Griffey Jr. 3 lowest total in At-Bats: ', lowestTotalAtBats)

print(' ' * 45)
print('_' * 45)
print(' ' * 45)
print('_' * 45)
print(' ' * 45)

# program 4: calculate how many times he played at least 80% of games in a season
print('\nProgram 4: Calculating how many times he played at least 80% of games in a season')

eightySzn = 0.8 * 162
seasons = 0

for games in gamesPlayed:
    if games >= eightySzn:
        seasons += 1

print('\n The number of times Ken Griffey Jr. played at least 80% of games in a season: ', seasons)

print(' ' * 45)
print('_' * 45)
print(' ' * 45)
print('_' * 45)
print(' ' * 45)
