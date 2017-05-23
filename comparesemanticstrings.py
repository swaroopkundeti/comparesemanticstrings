import re
import sys


# str1 = sys.argv[1]
# str2 = sys.argv[2]
# str3 = sys.argv[3]


_REGEX = re.compile(r'''
	^(?:[v])?(?P<version>\d+\.\d+\.\d+){1}
	(?:-(?=\w+)|\.(?=\w+))?
	(?:(?P<pr>(?:0|[1-9A-Za-z-][0-9A-Za-z-]*)(\.(?:0|[1-9A-Za-z-][0-9A-Za-z-]*))*))?
	(\+(?P<build>[0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*
	))?$''',re.VERBOSE)  

# Private fuction to parse the version of the strings


def _parse(version):
   
    if version[0] == '0.0.0':
        raise exception("Not a valid version")

    return version


def compareversions(string1, rule, string2):

	string1 = string1.lower()
	string2 = string2.lower()

	string1_check = _REGEX.match(string1)
	#print string1_check
	if not string1_check:
		 sys.exit('"%s" is not a valid semantic version' % string2)

	string2_check = _REGEX.match(string2)
	if not string2_check:
		sys.exit('"%s" is not a valid semantic version' % string2) 

	if rule == "==":
		return string1 == string2
	elif rule == ">":
		return string1 > string2
	elif rule == "<":
		return string1 < string2
	elif rule == ">=":
		return string1 >= string2
	elif rule == "<=":
		return string1 <= string2
	elif rule == "~>":
		string1_major = (string1[0].split('.'), string1[1], string1[2], )
		string2_major = (string2[0].split('.'), string2[1], string2[2], )

		# For comparing 2 versions with "~>" we need to match the major and 
		# version mentioned in file (Ex: requirements.txt/Gemfile) should be less than the new version

		return (string1_major[0][0] == string2_major[0][0] and string1 <= string2)
	else:
		print "Invalid rule"


# var = compareversions(str1, str2, str3)
# print var















