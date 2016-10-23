from bkp import opts
from bkp import bkp
from bkp import zip

src = "{}".format(opts.args.src)
dst = "{}".format(opts.args.dst)

if opts.args.zipfile:
	zip.compress(src, dst)
elif opts.args.backup:
	bkp.bkp(src, dst)
