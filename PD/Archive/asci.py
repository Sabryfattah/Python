import sys, re
file = sys.argv[1]

f = open(file, 'r')
text = f.read()
asci = re.sub(r'[^\x00-\x7f]',r'', text)
asci = "".join(i for i in text if ord(i)<128)
f.close()
with open(file, 'w') as f:
	f.write(asci)
	f.close()