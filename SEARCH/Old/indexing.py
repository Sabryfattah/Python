import os
from glob import glob
import sys
#========================================================
path = os.path.dirname(__file__)+"\\data\\"
def index(folder):
	idx_file = path+folder[3:]+".txt"
	if os.path.exists(idx_file):
		os.remove(idx_file)
	result = [y for x in os.walk(folder) for y in glob(os.path.join(x[0], "*.*"))]
	for f in result:
			open(idx_file, "a").write(f+"\n")
	print(("index  ===============   "+ idx_file + "  ============  created"))