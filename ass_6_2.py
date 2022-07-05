def rem_vowel(string):
	vowels = ['a','e','i','o','u']
	result = [letter for letter in string if letter.lower() not in vowels]
	result = ''.join(result)
	print(result)


string = "Sayani Ghatak from Jis university"
rem_vowel(string)
string = "sodepur sukchar park"
rem_vowel(string)
