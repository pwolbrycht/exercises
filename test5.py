# find all permutations of 'teststring' inside 'bigstring'
# example taken from HackerRank
import time


def permute(string, step=0):
    if step == len(string):
        perms.append("".join(string))
    for i in range(step, len(string)):
        string_copy = [char for char in string]
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        permute(string_copy, step+1)
    return perms


# strings to be tested
teststring = "xacxzaa"
bigstring = "fxaazxacaaxzoexazxaxaz"

# algorithm #1 - all permutations and searching through string
start = time.perf_counter()
perms = []
answer = []
listOfPerms = list(set(permute(teststring)))

for i in listOfPerms:
    if i in bigstring:
        answer.append(i)
end = time.perf_counter()
final_time = end-start

print(answer)
print("This algorithm took " + str(round(final_time, 6)) + " seconds.")

# algorithm #2 - looking for a window and testing 'is it a permutation?'
start2 = time.perf_counter()
secondAnswer = []
loopLength = len(bigstring) - len(teststring) + 2
sortedTestString = sorted(teststring)

for i in range(0, loopLength):
    a = bigstring[0+i:len(teststring)+i]
    if sorted(a) == sortedTestString:
        secondAnswer.append("".join(a))

end2 = time.perf_counter()
final_time2 = end2-start2
difference = final_time/final_time2

print(secondAnswer)
print("This algorithm took " + str(round(final_time2, 6)) + " seconds.")
print("Second algorithm is " + str(round(difference)) + "x faster than first one.")
