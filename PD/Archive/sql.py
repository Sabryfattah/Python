"""BASIC SQL BUILDING TOOL :
Can be imported to any sqlite script to add more functions such as:
1- Create New databse file or delete database file
2- Create new table in Database file or delete table
3- Rename Table.
4- List Tables in Database file.
5- Read a csv file and insert its data into table.
6- Write table to CSV file.
7- Get Column Names.
8- Duplicate table by copying it to another.
9- Add column to end of table.
10- Create a child table.

USE:
from sql import *
SQL(db_file, table).method()
"""
#=================================================================
import sqlite3
import re,os
import argparse
import csv
import glob
#===================== ARGPARSE =======================================
def argpar():
	parser = argparse.ArgumentParser(
		formatter_class=argparse.RawDescriptionHelpFormatter,
		description = __doc__,
		usage="sql <path> <table> <options>")
	parser.add_argument('path', nargs ="?", action='store', help='path to db file')
	parser.add_argument('table', nargs ="?", action='store', help='table to open')
	parser.add_argument('-a', '--all' , action='store_true', help='print table')
	parser.add_argument('-ac', '--addcol' , action='store_true', help='add column to end of table')
	parser.add_argument('-c', '--cols' , action='store_true', help='column headers')
	parser.add_argument('-cr', '--create' , action='store_true', help='create table')
	parser.add_argument('-dl', '--delete' , action='store_true', help='delete table')
	parser.add_argument('-l', '--list' , action='store_true', help='list tables in db_file')
	parser.add_argument('-rg', '--regex' , action='store_true', help='regex search')
	parser.add_argument('-n', '--notes' , action='store_true', help='display_as_notes')
	parser.add_argument('-m', '--multi' , action='store_true', help='update multiple rows')
	parser.add_argument('-rc', '--rencol' , action='store_true', help='rename columns')
	parser.add_argument('-rn', '--rename' , action='store_true', help='rename table')
	parser.add_argument('-w', '--write' , action='store_true', help='write table to csv')
	parser.add_argument('-v', '--readcsv' , action='store_true', help='read csv into table')
	args = parser.parse_args()
	return args
##########################################################################

def get_cols(path,table):
	" GET NAMES OF COLUMNS (HEADERS)  "
	cols = []
	db = sqlite3.connect(path)
	cursor = db.cursor()
	cursor.execute("PRAGMA table_info({})".format(table))
	hd = cursor.fetchall()
	for header in hd:
		cols.append(str(header[1]))
	return cols

def col_names(path,table):
	" GET HEADERS AS COLUMNS NAMES "
	conn = sqlite3.connect(path)
	cursor = conn.execute('select * from {}'.format(table))
	cols =  list([x[0] for x in cursor.description])
	return cols

def create_table(path,table):
	"headers of Table as string "
	headers =input("Enter headers of table separated by commas ..>\n").split(",")
	"types of fields"
	types = input("Enter types of headers separated by commas ..>\nNULL,INTEGER,TEXT,REAL(i.e.float),BLOB\n").split(",")
	colns = []
	"first line"
	t = "CREATE TABLE {}".format(table)
	"second line, id and primary key"
	id = "ID INTEGER PRIMARY KEY AUTOINCREMENT"
	"headers and types "
	for n in range(len(headers)):
		colns.append("{c}	{p},".format(c=headers[n],p=types[n]))
	c =  "\n".join(colns)
	exdoc = "{} ({},\n{}".format(t,id,c[:-1])
	db = sqlite3.connect(path)
	db.execute( """{})""".format(exdoc))
	db.commit()
	db.close()
	print(("TABLE {t} created in the form of:\n {c}".format(t=table, c=exdoc)))

def list_tables(path,table):
	"List tables in db file "
	conn = sqlite3.connect(path)
	tables = conn.execute("select name from sqlite_master where type = 'table';")
	print("="*35)
	print("TABLES in {}". format(path))
	print("="*35)
	for table in tables:
		print("\n".join(table))
	print("-"*35)
	conn.close()

def print_all():
	"print all rows in table "
	cols = col_names()
	conn = sqlite3.connect(path)
	cursor = conn.execute("SELECT * FROM {t}".format(t=table))
	rows = cursor.fetchall()
	"create a list for column sizes"
	all_columns_sizes = []
	"create form string for formatting"
	form = []
	"iterate over number of columns "
	for n in range(len(cols)):
		"create a list to store size of each row for each column "
		column_length = []
		for row in rows:
			" got through each row list and get its size for that column"
			column_length.append(len(str(row[n])))
			"add max of that_column_length to all_columns_sizes"
		all_columns_sizes.append(str(max(column_length)))
	for n in range(len(cols)):
		form.append("{:<%s}  " % all_columns_sizes[n])
	form = "".join(form)
	print("="*90)
	print(form.format(*cols))
	print("-"*90)
	for row in rows:
		print(form.format(*row))
	print("="*90)

def drop_table():
	"Delete a table "
	db = sqlite3.connect(path)
	cursor = db.cursor()
	table_dropped = input("Table to delete from Database ....")
	print(("ARE YOU SURE YOU WANT TO DELETE {} TABLE !!".format(table_dropped)))
	input('Press enter to continue: ')
	cursor.execute("""DROP TABLE {}""".format(table_dropped))
	db.commit()
	db.close()

def dup_tab():
	"COPY TABLE TO ANOTHER DB "
	"ATTACH DATABSE to ANOTHER and INSERT COLUMNS THEN DETACH THE OTHER "
	source_db = input("Enter name of source database\n")
	dest_file = input("Enter name of destination database\n")
	dest_cols = input("Enter Destination columns separated by commas..")
	src_cols = input("Enter Source columns separated by commas..")
	src_table = input("Enter Source table\n")
	destable = input("Enter destination table\n")
	path =  '/PY/SQL/DB/'
	src = '{p}{f}.db'.format(p=path,f=source_db)
	conn = sqlite3.connect(src)
	cursor = conn.cursor()
	conn.execute("ATTACH DATABASE '{p}{f}.db'  AS other ".format(p=path,f=dest_file))
	cursor.execute("INSERT INTO other.{dt} ({df}) SELECT {sc} FROM {st}".format(df=dest_cols,sc=src_cols,st=src_table,dt=destable))
	conn.execute("DETACH other;")
	cursor.close()
	conn.close()

def read_csv():
	"""Read a csv file and insert its data into table created above """
	data = []
	cols = col_names()
	db = sqlite3.connect(path)
	db.text_factory = str
	cursor = db.cursor()
	filename = input("Put csv file in sql/csv/\nEnter csv file name without ext..>\n")
	d = "sql/csv/"
	file ="{}{}.csv".format(d,filename)
	rows = open(file, 'r').readlines()
	for n,row in enumerate([_f for _f in rows if _f]):
		row = row.strip("\n")
		parts = row.split(",")
		#print n, len(parts) #use to check if number of columns in csv file incorrect
		data.append(parts)
	data = [x for x in data]
	col = ",".join(cols[1:])
	cursor.executemany("INSERT INTO {t} ({col}) VALUES (?,?,?,?,?,?,?,?)".format(t=table,col=col), (data))
	db.commit()
	print(("'{}' imported into table '{}' in db file '{}'".format(file,table,db_file)))
	db.close()

def write2csv():
	"WRITE DB TABLE TO CSV FILE "
	csvWriter = csv.writer(open(table+".csv", "w"))
	conn = sqlite3.connect(path)
	c = conn.cursor()
	r = c.execute("SELECT * FROM {}".format(table))
	rows = r.fetchall()
	csvWriter.writerows(rows)
	conn.close()

def rename_cols():
	cols = col_names()
	print(",".join(cols))
	form = []
	new_cols = input("Enter new colums separated by commas :  >>\n")
	for element in zip(cols, new_cols.split(",")):
		form.append("{} as {} ".format(element[0], element[1]))
	form = ", ".join(form)
	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	cursor.execute(
	"CREATE table {t}_tmp as SELECT {f} FROM  {t};".format(f=form,t=table))
	cursor.execute("DROP table {};".format(table))
	cursor.execute("ALTER table {t}_tmp rename to {t};".format(t=table))
	cursor.close()
	conn.close()

def add_column():
	"add a column to end of table "
	new_col_name = input("Enter New Column Name:......>\n")
	width = input("Enter width of new column :......>\n")
	conn  = sqlite3.connect(path)
	cursor  = conn.cursor()
	cursor.execute("ALTER TABLE {t} ADD COLUMN  {c} VARCHAR({w})".format(t=table, c=new_col_name, w=width))
	cursor.close()

def create_child_table():
	table_name = input("Enter child table name ...>")
	headers =input("Enter headers of child table separated by commas ..>\n").split(",")
	types = input("Enter types of headers of child table separated by commas ..>\n").split(",")
	Parent = input("Enter Parent table to link to child table:..>\n")
	shared_field = input("Enter shared_field to link the two tables:..>\n")
	fkey = "FOREIGN KEY ({sh}) REFERENCES {P}({sh})".format(P=Parent,sh=shared_field)
	colns = []
	t = "CREATE TABLE {}".format(table_name)
	id = "ID INTEGER PRIMARY KEY AUTOINCREMENT"
	for n in range(len(headers)):
		colns.append("{c}	{p},".format(c=headers[n],p=types[n]))
	c =  "\n".join(colns)
	exdoc = "{} ({},\n{}\n{}".format(t,id,c,fkey)
	print(exdoc)
	db = connect2db()
	db.execute( "{})".format(exdoc))
	db.commit()
	db.close()

def re_fn(expr, item):
	reg = re.compile(expr, re.I)
	return reg.findall(item, re.I) is not None

def regex_query():
	"Select records by Regex pattern using function above "
	pat = input("Regex pattern: ? >   ")
	col = input("Column Name ? >    ")
	SEARCH_TERM = pat
	conn = sqlite3.connect(db_file)
	conn.create_function("REGEXP", 2, re_fn)
	conn.create_function('regexp', 2, lambda x, y: 1 if re.search(x,y,re.I) else 0)
	cursor = conn.cursor()
	cursor.execute(
	'SELECT * FROM {t} WHERE {c} REGEXP ?'.format(t=table, c= col), [SEARCH_TERM]
	)
	conn.commit()
	cols =  list(map(lambda x: x[0], cursor.description))
	rows =cursor.fetchall()
	print("="*80)
	form = "{:<}    "*len(cols)
	print(form.format(*cols))
	print("-"*80)
	for row in rows:
		print(form.format(*row))
	print("="*80)

def display_as_notes():
	conn = sqlite3.connect(path)
	cursor = conn.execute("SELECT * FROM {}".format(table))
	rows = cursor.fetchall()
	cols = col_names()
	print("="*80)
	print(*cols)
	for row in rows:
		for n in range(len(cols)):
			print("{:<10} : {r}".format(cols[n], r=row[n]))
			print("-"*80)
		print("="*80)

def multi_update():
	"update multiple rows with same value"
	cols = col_names()
	conn = sqlite3.connect(path)
	pls = "| {} |"*len(cols)
	colnames = "Column Title to update ? >\n"+pls+"\n "
	print(colnames.format(*cols))
	colnam = input("Column Name to update ..>\n")
	pat = input("Pattern in rows to update : multiple strings separated by spaces\n>")
	cursor = conn.execute("SELECT * FROM  {t} where {cc} LIKE '%{p}%'".format(t=table,cc=colnam,p=pat))
	print_all()
	val1 = input("Original Value to update ? >\n")
	val2 = input("New value to enter ? >\n")
	conn.execute("UPDATE  "+table+" SET "+colnam+ " = ? WHERE "+colnam+" =  ? ", (val2,val1))
	print("Total number of rows updated :", conn.total_changes)
	conn.commit()
	print("Update done successfully");
	conn.close()

def write2csv():
	csvWriter = csv.writer(open(table+".csv", "w"))
	conn = sqlite3.connect(path)
	c = conn.cursor()
	r = c.execute("SELECT * FROM {}".format(table))
	rows = r.fetchall()
	csvWriter.writerows(rows)
	conn.close()

def read_csv():
	"Read a csv file and insert its data into table created above "
	path = "sql/csv/"
	file = input("Enter csv file without ext : default path = c:/py/sql/csv/\n")
	csv_file = path+".csv"+file
	rows = open(csv_file, 'r').readlines()
	for row in rows[1:]:
		r = row.strip().split(",")
		data.append(tuple(r))
	db = sqlite3.connect(path)
	cols = col_names()
	cols = ",".join(cols)
	cursor = db.execute("SELECT * FROM {t}".format(table))
	cursor.executemany("INSERT INTO  {t}  ({cc}) VALUES (?,?,?)".format(
	t=table, cc=cols), data)
	db.commit()
	db.close()

def rename_table():
	print("current db : {db} and current table : {t}".format(db=db_file,t=table))
	new_table_name = input("Enter New Table Name :......>\n")
	conn  = sqlite3.connect(path)
	cursor  = conn.cursor()
	cursor.execute("ALTER TABLE {} RENAME TO {}".format(table, new_table_name))
	cursor.close()
#############################################################################
if __name__ == "__main__" :
	args = argpar()
	path  = args.path
	table = args.table
	if args.list : list_tables(path,table)
	if args.cols : print(s.col_names())  #if s.args.cols : print(s.get_cols())
	if args.all : print_all()
	if args.create : create_table(path,table)
	if args.regex : regex_query()
	if args.notes : display_as_notes()
	if args.multi : multi_update()
	if args.write : write2csv()
	if args.readcsv : read_csv()
	if args.rename : rename_table()
	if args.delete : drop_table()
	if args.addcol : drop_table()
	if args.rencol : rename_cols()
