import sqlite3
from sqlite3 import Error

def create_connection(db_file):
	"Create Database"
	try:
		conn = sqlite3.connect(db_file)
		print(sqlite3.version)
	except Error as e:
		print(e)
	finally:
		conn.close()

if __name__ == '__main__':
	"Define DB Name (== company name)"
	co = input("Company:")
	"Define path where DB is saved (Feature to select path to be included)"
	create_connection("C:\\" + str(co) +str(".db"))

conn = sqlite3.connect("C:\\" + str(co) +str(".db"))
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS journal
			(number, dr_cr, account, account_description, value_date, posting_date, business_case, counterparty, doc_number, reference, text, \n
			move_type, doc_currency, amount_in_doc_currency, transactional_fx, amount_in_functional_currency, amount, tax_code, period)''')
conn.commit()
c.close
