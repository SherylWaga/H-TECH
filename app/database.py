import os
import psycopg2
connection = psycopg2.connect(dbname='htech', user='postgres', password='refuge', host='localhost')

def init_db ():
	conn = connection
	return conn


def create_table():
	queries = ("""
		CREATE TABLE IF NOT EXISTS users(
			user_id SERIAL PRIMARY KEY UNIQUE NOT NULL,
			first_name VARCHAR(50) NOT NULL,
			last_name VARCHAR(50) NOT NULL,
			username VARCHAR(50) NOT NULL,
			phone INT,
			email VARCHAR(250) NOT NULL,
			password VARCHAR(250) NOT NULL,
			confirmed BOOLEAN DEFAULT False,
			is_admin BOOLEAN DEFAULT False);""",

				"""CREATE TABLE IF NOT EXISTS tests(
			tests_id SERIAL PRIMARY KEY UNIQUE NOT NULL,
			un_id INT,
			tests VARCHAR(50) NOT NULL,
			results  VARCHAR(250),
			created_on TIMESTAMP DEFAULT NOW()
			);"""

				"""CREATE TABLE IF NOT EXISTS pattient(
			pattient_id SERIAL PRIMARY KEY UNIQUE NOT NULL,
			un_id INT,
			first_name VARCHAR(50) NOT NULL,
			last_name VARCHAR(50) NOT NULL,
			email VARCHAR(50),
			id_number INT,
			phone_number INT,
			age INT,
			weight INT,
			location VARCHAR(50) NOT NULL,
			next_appointment VARCHAR(50),
			created_on TIMESTAMP DEFAULT NOW()
		);""")
	connection = init_db()
	curr = connection.cursor()
	for query in queries:
		curr.execute(query)
	connection.commit()


def drop_table():
	""" Methon for droping table """
	connection = init_db()
	curr = connection.cursor()

	queries = (
		"""DROP TABLE IF EXISTS users CASCADE;""", """DROP TABLE IF EXISTS tests CASCADE;""",\
		"""DROP TABLE IF EXISTS pattient CASCADE;""")
	for query in queries:
		curr.execute(query)
		connection.commit()

def close_instance():
	connection = init_db()
	curr = connection.cursor()
	connection.close()
	curr.close()

def admin():
	connection = init_db()
	curr = connection.cursor()

	first_name = 'admin'
	last_name =  'wise'
	username  = 'admin'
	phone = '0725696042'
	email = 'admin@admin.com'
	password = 'admin@wise'
	confirmed=True
	is_admin=True

	sql = "SELECT * FROM users WHERE username = %s"
	curr.execute(sql, (username,))
	data = curr.fetchone()

	if not data:
		sql = """INSERT INTO users(first_name, last_name, username, phone, email, password, confirmed, is_admin)\
					VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""
		curr.execute(sql, (first_name, last_name, username, phone, email, password, confirmed, is_admin))
	connection.commit()