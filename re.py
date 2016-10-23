import re 
 
#Determine if the RE matches at the beginning of the string ==>
p = re.compile("\w+")
m = p.match('Hello World')
if m:
    print 'Match found: ', m.group()
else:
    print 'No match'
	
#Search through string for a match ==>
p = re.compile("\w+")
print p.search('Hello World').group()

#Findall matches in  string for a match ==>
p = re.compile('\d+')
print p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
r = p.finditer('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
for i in r:
	print i.group()
	print i.start()
	print i.end()
	print i.span()
  


p = re.compile(r'\bclass\b')
print p.search('no class at all').group()  
print p.search('the declassified algorithm')
print p.search('one subclass is')


p = re.compile('(ab)*')
print p.match('ababababab').span()

p = re.compile('(a)b')
m = p.match('ab')
print m.group()
print m.group(0)
print m.group(1)

p = re.compile('(a(b)c)d')
m = p.match('abcd')
print m.group(0)
print m.group(1)
print m.group(2)
print m.group(2,1,2)

p = re.compile(r'(\b\w+)\s+\1')
print p.search('Paris in the the spring').group()


m = re.match("([abc])+", "abc")
m.groups()
m = re.match("(?:[abc])+", "abc")
print  m.groups()

p = re.compile(r'(?P<word>\b\w+\b)')
m = p.search( '(((( Lots of punctuation )))' )
print m.group('word')
print m.group(1)


p = re.compile(r'\W+')
p.split('This is a test, short and sweet, of split().')
p.split('This is a test, short and sweet, of split().', 3)

p = re.compile('(blue|white|red)')
print p.sub('colour', 'blue socks and red shoes')
print p.sub('colour', 'blue socks and red shoes', count=1)

p = re.compile('(blue|white|red)')
print p.subn('colour', 'blue socks and red shoes')
print p.subn('colour', 'no colours at all')