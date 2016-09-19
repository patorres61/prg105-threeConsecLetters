# This program will read a text file of words and find words that have three consecutive double letters

# Define variables
tripleLetterWords = 0
noTripleConsec = 0
totalWords = 0

# Define input file
fin = open('words.txt')

print ('Words Containing Three Consecutive Double Letters\n')

# Read file, check character count in each line
def has_trip_consec(word):
    index = 0                   # initialize index to systematically check for consecutive letters in a word
    cntletters = 0              # initialize the counter to check for three consecutive double letters
    while index < len(word)-1:  # make sure index is less than the length of the word
        if word[index] == word[index+1]:    # compare two consecutive letters in a word
            cntletters += 1
            if cntletters == 3:
                return True
            index += 2          # add 2 to index to move to next two letters in word
        else:
            cntletters = 0      # a non-match of letters resets the count of consecutive letter pairs
            index += 1
    return False

for line in fin:
    word = line.strip()  # line.strip will strip out any blank spaces
    totalWords += 1         # accumulate total number of words in file
    if has_trip_consec(word):  # code to handle when triple consecutive double letters condition found
        print word
        tripleLetterWords += 1
    else:
        noTripleConsec += 1

print ('\nTotal number of words in file containing three consecutive double letters: ' + str(tripleLetterWords))
print ('\nTotal words in file NOT containing three consecutive double letters: ' + str(noTripleConsec))
print ('\nTotal number of words in file: ' + str(totalWords))

