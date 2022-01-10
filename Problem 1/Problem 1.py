# Michael Williamson
# 1/10/2022
# Given a text input, find the longest word and output it.
# Sample Input: "This is an awesome text" -> Sample Output: "awesome"
import time
start_time = time.time()

test = "this is an awesome text"

# First attempt
test_split = test.split()

longest = ''

for item in test_split:
    if len(item) > len(longest):
        longest = item

print("Longest word is: ", longest)
print("And its length is: ", len(longest))
print("--- %s seconds ---" % (time.time() - start_time))