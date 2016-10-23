import opts
from os import path
from os import walk
import shutil
#==============================================================
src = "{}".format(opts.args.src)
dst = "{}".format(opts.args.dst)
FILES = []
DIRS = []
#===================================================
def get_file_dirs(path):
	tree = os.walk(path, topdown=False)
	for d in tree:
		DIRS.append(d[0])
		for f in d[2]:
			FILES.append(d[0]+"\\"+f)
	return [FILES, DIRS]
#===================================================
def make_dirs(path):
	directories = get_file_dirs(path)[1]
	for d in directories:
		dstdir = DRIVE+d[1:]
		if not os.path.exists(dstdir):
			os.makedirs(dstdir)
#===================================================
def copy_files(path):
	files = get_file_dirs(path)[0]
	for f in files:
		dstfile = DRIVE+f[1:]
		if not os.path.exists(dstfile):
			shutil.copy(f, dstfile)
			print "now copying : "+f+"  to ===>"+dstfile
#============================================
def bkp():
	get_file_dirs(PATH)
	make_dirs(PATH)
	copy_files(PATH)
#=============================================
bkp()
