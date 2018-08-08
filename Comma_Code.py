# Comma Code Program
# Neeraj Nair
# Chapter 4

def fn_spam(spam):
	last_part = spam.pop()
	first_part = ','.join(spam)
	print( first_part + " and " + last_part )


