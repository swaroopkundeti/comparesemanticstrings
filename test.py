from comparesemanticstrings import compareversions
import sys



str1 = sys.argv[1]
str2 = sys.argv[2]
str3 = sys.argv[3]

var = compareversions(str1, str2, str3)

print var