from sys import stdout

import xmltodict
import gzip
import json

count = 0
xmlSrc = 'xml/cd.xml.gz'
jsDest = 'js/cd.js'

# define a function to parse each individual node
def parseNode(_, node):
	global count
	count += 1
	stdout.write("\r%d" % count)

	jsonNode = json.dumps(node)
	f.write(jsonNode + '\n')
	return True


# create and open an output file
f = open(jsDest, 'w')

# stream through file
xmltodict.parse(gzip.open(xmlSrc), item_depth=2, item_callback=parseNode)

f.close()

stdout.write("\n") # move the cursor to the next line