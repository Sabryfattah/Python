import os,sys
pat = sys.argv[1]
os.system("grep -rI -w -h -B 1 -A 12 -i {}  E:/confidential".format(pat))