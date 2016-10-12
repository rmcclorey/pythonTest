#enter string returns reversed string
def reverseString(str):
	return str [::-1]

print reverseString("Hello World")

#enter single word string returns pig latin form
def pigLatin(str):
	return str[1:]+str[0]+"ay"

print pigLatin("Hello")

#enter string returns how many vowels present
def vowelCounter(str):
	vowels = ["a","e","i","o","u"]
	counter = 0
	for char in str:
		if char in vowels:
			counter += 1
	return counter 

print vowelCounter("Hello World")

#enter string returns if palindrome or not
def palindromeChecker(str):
	if str == str[::-1]:
		return "True"
	else:
		return "False"

print palindromeChecker("racecar")
print palindromeChecker("Hello World")

#enter string returns the amount of characters
def wordCounter(str):
	return len(str)

print wordCounter("Hello World")