import urllib

def read_text():
	quotes = open(".\movie_quotes.txt")
	contents_of_file = quotes.read()
	# print (contents_of_file)
	quotes.close()

	check_profanity(contents_of_file)

def check_profanity(text):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
	output = connection.read()
	print (output)
	connection.close()

read_text()