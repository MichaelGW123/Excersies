# Michael Williamson
# 1/10/2022
# Given a text input, find the longest word and output it.
# Sample Input: "This is an awesome text" -> Sample Output: "awesome"
import time
start_time = time.time()

# Second attempt
longest = ''
with open('C:\\Users\Michael JITN\\Documents\\Work\\Arete Interview\\Excersies\\Problem 1\\test.txt', 'r') as file:
    for line in file:
        for word in line.split():
           if len(word) > len(longest):
                longest = word

print("Longest word is: ", longest)
print("And its length is: ", len(longest))
print("--- %s seconds ---" % (time.time() - start_time))