#!/usr/bin/python3
# Importing the 'cgi' module
import cgi
import random
from secondPy import bigHomie

def outputName():
	output = ['savannah is dumb', 'ur a ugly poo monkey', 'i fart on thee']
	x = random.choice(output)
	return x

#sets how i want to display the webpage
print("Content-type: text/html\r\n\r\n")
print("<html><body>")
output = outputName()
print("<b><p>"+output + "</b></p>")
list = bigHomie()
for text in list:
	print("<p>" + text + "</p>")

# Using HTML input and forms method
print("<form method='post' action='test.py'>")
print("<p>write stuff here: <input type = 'text' name = 'n1'/></p>")
print("<input type='submit' name='submit' value='Submit' />")
print("</form")

form = cgi.FieldStorage()
if form.getvalue("n1"):
	text = form.getvalue("n1")
	with open('test.txt', 'a') as f:
		f.write(text + "\n") 
	print("<p>" + text+"</p>")

print("</body></html>")

