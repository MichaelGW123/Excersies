# Michael Williamson
# 1/10/2022
# Given the quote: "Always do your best. Your best is going to change from moment to moment;
# it will be different when you are healthy as opposed to sick. Under any circumstance, simply do
# your best, and you will avoid self-judgment, self-abuse and regret." Complete the program so
# that it will take a word as input and output the number of times that word appears in the
# quote.
# Sample Input: "best" -> Sample Output: 3
import time
import string
start_time = time.time()

# First attempt

target = 'fry'
count = 0
with open('C:\\Users\Michael JITN\\Documents\\Work\\Arete Interview\\Excersies\\Problem 2\\test.txt', 'r') as file:
    for line in file:
        line_stripped = line.translate(str.maketrans('', '', string.punctuation))
        for word in line_stripped.split():
           if word == (target):
                count+=1

print("Target word is: ", target)
print("And its occurences: ", count)
print("--- %s seconds ---" % (time.time() - start_time))