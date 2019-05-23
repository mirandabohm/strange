import re 

def validate_username(username):
	'''Checks that a valid username has been entered. Must not be blank. WORKING'''
	pattern = "^[a-zA-Z0-9_-]{3,20}$"
	b = re.search(pattern, username)
	if b and username !="":
		username = True
	else:
		username = None
	return username

def validate_password(password):
	if password != '':
		if ' ' in password:
			valid = False
		else:
			valid = True
	else:
		valid = None
	return valid

def validate_verify(password, verify):
	'''Checks to see if passwords match.'''
	# password != '' and verify != '' and 
	if str(verify) == str(password):
		matching = True
	elif str(password) != str(verify):
		if password != '':
			matching = False
		else:
			matching = None
	else:
		matching = None
	return matching

def validate_email(email):
	'''Checks email against a standard format. Returns 0 if
	email does not match and 1 if there is a match.'''
	tldomains = ['com', 'org', 'net', 'int', 'edu', 'gov', 'mil']
	patterns = ['[A-Za-z0-9]*@[A-Za-z0-9]*\.' + tld for tld in tldomains]

	matches = False
	for pattern in patterns: 
	    b = re.search(pattern, email)
	    if b: 
	        matches = True
	if matches:
	    print('Success!\nMatches:', matches)
	return matches