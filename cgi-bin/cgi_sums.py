#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
operands = form.getlist('operand')

total = sum(map(int, operands))
body = "Your total is {}".format(total)

print("Content-type: text/plain")
print()
print(body)
