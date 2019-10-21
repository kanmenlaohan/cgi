#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

# Sample error to trigger cgitb
# 1/0

cgi.test()
