""" CONVERT CSV FILE TO YAML """
import csv, glob

def get_files():
	files = glob.glob("*.csv")
	return files

def from_csv_to_yaml():
	n = 0
	files = get_files()
	for file in files:
		csvfile = open(file, "r" ).readlines()
		hd = csvfile[0].strip().split(",")
		f = open('{}.yaml'.format(file[:-4]), 'w')
		f.write("---\n")
		f.write('#filename : {}\n'.format(file[:-4]))
		for i, row in enumerate(csvfile[1:]):
			csv_content = row.strip().split(",")
			f.write("{}: \n".format(csv_content[0]))
			n = 1
			print(hd)
			while n <  len(hd):
				f.write(' - {}: {}\n'.format(hd[n], csv_content[n]))
				n += 1
				#f.write(' - {}: {}\n\n'.format(hd[3], csv_content[3]))
		f.write('...')
		f.close()


from_csv_to_yaml()