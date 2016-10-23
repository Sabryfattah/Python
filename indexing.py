import os
from glob import glob
import sys
#========================================================
folder = "D:\Documents"

result = [y for x in os.walk(folder) for y in glob(os.path.join(x[0], "*.txt"))]
for f in result:
	open("index.txt", "a").write(f+"\n")