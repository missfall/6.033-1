import re

def read_file(filename):
	with open(filename, 'r') as f:
		fr = fd.read()
		return re.sub( r'execfile\(\'new_shell\.py\)\n', '', read)

def login(args):
    if len(args) != 1:
        raise CommandError("Usage: login username")

    global username
    if username:
        raise CommandError("Already logged in.")
    username = args[0]

   	with open("usernames.txt", 'a') as fa:
   		fa.write(username + "\n")