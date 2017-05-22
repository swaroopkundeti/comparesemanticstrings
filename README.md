# comparing semantic version

This library is written in python 2.7 and it will require to pass 3 variables *"string1"* *"rule"* and *"string2"* to test comparisions of sematic versions. We can test in different ways.

## with a test.py

<pre>python test.py "1.2.3" "==" "1.2.4"
False</pre>

## with python interpretor
<pre>
	>>> import sys
	>>> sys.path.append('/Users/swaroopkundeti/Documents/comparesemanticstrings') # Please alter the path accordingly
	>>> from comparesemanticstrings import compareversions
	>>>
	>>> var = compareversions("1.2.3", "==", "1.2.4")
	>>> print var
	False
	>>>
	>>> var = compareversions("1.2.3", ">=", "1.2.4")
	>>> print var
	False
	>>> var = compareversions("1.2.3", "<=", "1.2.4")
	>>> print var
	True
	>>> var = compareversions("1.2.3", "<", "1.2.4")
	>>> print var
	True
	>>> var = compareversions("1.2.3", "~>", "1.2.4")
	>>> print var
	True
</pre>

