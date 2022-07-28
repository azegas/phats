import re

filename = r'files/pvz.txt'

string = open(filename).read()
new_str = re.sub('3', '', string)
open(filename, 'w').write(new_str)
