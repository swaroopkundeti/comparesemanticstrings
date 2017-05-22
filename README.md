# semanticversion-python

* This library is written in python 2.7 and it will require to pass 3 variables string1 rule and string2 to test comparisions of sematic versions. We can test in different ways.

** Through a test.py which takes 3 strings in a strict way like "string1" "rule" "string2"

<pre>python test.py "1.2.3" "==" "1.2.4"</pre>

** Through python interpretor
<pre>
	>>> import sys
	>>> sys.path.append('/Users/swaroopkundeti/Documents/comparesemanticstrings')
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

