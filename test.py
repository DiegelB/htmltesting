#!/usr/bin/python3
# Importing the 'cgi' module
import cgi

#sets how i want to display the webpage
print("Content-type: text/html\r\n\r\n")
print("<html><body>")
print("<h1> Test Program </h1>")




# Using HTML input and forms method
print("<form method='post' action='test.py'>")
print("<p>Number 1: <input type='number' name='n1' /> </p>")
print("<p>Number 2: <input type = 'number' name ='n2' /> </p>")

print("<input type='submit' name='submit' value='Submit' />")

print("</form")
print("</body></html>")

form = cgi.FieldStorage()
if form.getvalue("n1"):
	num1 = form.getvalue("n1")
if form.getvalue("n2"):
	num2 = form.getvalue("n2")
total = int(num1) + int(num2)
print("<p>total: " + str(total)+ "</p>")