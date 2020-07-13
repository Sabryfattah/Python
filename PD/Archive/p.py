"""SQLITE DB Script to display all monthly bills and annual cost """
import sqlite3
import re, os
import argparse
import glob
from sql import *
#======================= CLASS BILLS ==========================
class Bills():
	def __init__(self, db_file=None, table = None, cols=None):
		self.db_file = "SQL/DB/wgdp.db" #Database filename
		self.table = "gdp" #table name
		self.parser = argparse.ArgumentParser(
			formatter_class=argparse.RawDescriptionHelpFormatter,
			description = __doc__,
			usage="bills <options>")
		self.parser.add_argument('-a', '--all' , action='store_true', help='print all rows of table')
		self.parser.add_argument('-i', '--insert' , action='store_true', help='insert data in table')
		self.parser.add_argument('-q', '--query' , action='store_true', help='query of table')
		self.parser.add_argument('-u', '--update' , action='store_true', help='update row in table')
		self.parser.add_argument('-ds', '--display' , action='store_true', help='display table')
		self.parser.add_argument('-d', '--delete' , action='store_true', help='delete row in table')
		self.args = self.parser.parse_args()
		self.cols = col_names(self.db_file,self.table)

	def print_all(self):  #PRINT ALL ROWS
		conn = sqlite3.connect(self.db_file)
		cols = self.cols
		cursor = conn.execute("SELECT * FROM {}".format(self.table))
		print("="*80)
		print("{:<10}{:<20}{:<20}{:<15}".format(cols[0],cols[1],cols[2],cols[3]))
		print("-"*80)
		for row in cursor:
			print("{:<10}{:<20}{:<20}{:<15}".format(row[0],row[1],row[2],row[3]))
		print("="*80)
		conn.close()

	def query(self): #QUERY Database
		conn = sqlite3.connect(self.db_file)
		cols = self.cols
		pat = input("Pattern to search for ..>  ")
		cursor = conn.execute("SELECT *  FROM  bills where Provider LIKE '%{p}%'".format(p=pat) )
		print("="*80)
		print("{:<5}{:<15}{:<20}{:<10}{:<10}".format(cols[0],cols[1],cols[2],cols[3],"Annual"))
		print("-"*80)
		for row in cursor:
			print("{:<5}{:<15}{:<20}{:<10}{:<10}".format(row[0],row[1],row[2],row[3],row[3]*12))
		total = conn.execute("Select Monthly FROM  Bills ")
		print("="*80)
		print("Total :{:>39.2f}".format(sum([x[0] for x in total])))
		print("-"*80)
		conn.close()

	def update(self):  #UPDATE TABLE 
		"modify and change data in one of the columns at row selected by ID "
		self.print_all()
		conn = sqlite3.connect(self.db_file)
		col = input("Column Title to update ? >  ")
		id = eval(input("ID number of row ?  >  "))
		val = input("Value to enter ? >  ")
		conn.execute("UPDATE "+self.table+" SET "+col+ " = ? WHERE id= ? ", (val,id))
		print("Total number of rows updated :", conn.total_changes)
		conn.commit()
		print("Update done successfully");
		conn.close()

	def insert_data(self): #INSERT NEW ROW
		"Insert a single row into the table selected in this method, fields should be as above "
		conn = sqlite3.connect(db_file)
		row_values = input("Enter values of row separated by comma ...\n Provider,Service,Monthly\n")
		row = tuple(row_values.split(","))
		conn.execute("INSERT INTO Home (Provider,Service,Monthly) \
		  VALUES {}".format(row));
		conn.commit()
		print("Record created successfully");
		conn.close()

	def delete(self): #DELETE ROW
		"Delete a row selected by ID"
		print(self.cols)
		conn = sqlite3.connect(self.db_file)
		id = input("ID number of row to delete ? > ")
		conn.execute("DELETE  from gdp WHERE index = {i}".format(i=id))
		conn.commit()
		print("Total number of rows deleted :", conn.total_changes)
		conn.close()
#========================  CALL FUNCTIONS =============
if __name__ == "__main__":
	t = Bills()
	if t.args.all: t.print_all()
	if t.args.insert: t.insert_data()
	if t.args.query: t.query()
	if t.args.update: t.update()
	if t.args.delete: t.delete()
	if  t.args.display: 
		db_file = "Home.db" #Database filename
		table = "bills" #table name
		sql = SQL(db_file, table)
		sql.display_table()