from tan import opts
from tan import ta
from tan import fa
from tan import wf

if opts.args.polarity:
	ta.polarity()
elif opts.args.word_analysis:
	fa.word_count()
elif opts.args.word_frequency:
	wf.word_freq()