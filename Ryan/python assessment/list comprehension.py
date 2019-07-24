"""
I made some up for you!

Find all of the numbers from 1-1000 that are divisible by 7

Find all of the numbers from 1-1000 that have a 3 in them

Count the number of spaces in a string

Remove all of the vowels in a string

Find all of the words in a string that are less than 4 letters

Challenge:

Use a dictionary comprehension to count the length of each word in a sentence.

Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)

For all the numbers 1-1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by

If you can solve the challenge ones, I think you can safely say you have it down.


level 2
Comment deleted by user
3 years ago
(More than 1 child)


level 2
Jon003
jon003
3 points
·
3 years ago
·
edited 3 years ago
Answered all of them:

https://gist.github.com/jon003/c51fa0523e1ac267b79550ea24c6ce4c

Continue this thread

# """
# a = [i for i in range(10)]
# print(a)
# #
# divisible_7 = [n for n in range(1000) if n % 7 == 0]
#
# have_3 = [n for n in range(1, 1001) if '3' in str(n)]
# results = [num for num in range(1000) if '3' in list(str(num))]
#
# count =[c for c in "dfs 23 23 2" if c == ' ']
#
# no_vowels = [ c for c in "this is a good book" if c not in ['a', 'e', 'i', 'o', 'u']]
#
# less_4 = [word for word in "this is a good book".split(" ") if len(word) < 4]


# CHALLENGE!
#Use a dictionary comprehension to count the length of each word in a sentence.
sentence = 'Use a dictionary comprehension to count the length of each word in a sentence'
results = {word:len(word) for word in sentence.split()}
#print(results)


number = [i for i in range(5)]
a=[True for divisor in range(2,10) if number % divisor == 0]

#Use a nested list comprehension to find all of the numbers from 1-1000 that
#are divisible by any single digit besides 1 (2-9)
# comprehension testing truth for divisibilty: [True for divisor in range(2,10) if number % divisor == 0]
results = [number for number in range(1,1001) if True in [True for divisor in range(2,10) if number % divisor == 0]]
#print(results)



#For all the numbers 1-1000, use a nested list/dictionary comprehension to
#find the highest single digit any of the numbers is divisible by.
# List comprehension for providing a list of all of the numbers a number is divisible by: divisor_list:
#       [divisor for divisor in range(1,1001) if number % divisor == 0]
results = {number:max([divisor for divisor in range(1,10) if number % divisor == 0]) for number in range(1,1001)}
#print(results)

1==1
