import sqlite3

db_path = "../links.db"

def generate_db():
	con = sqlite3.connect(db_path)
	cur = con.cursor()
	cur.execute("CREATE TABLE links(url)")
	con.commit()
	con.close()

def drop_links_table():
	con = sqlite3.connect(db_path)
	cur = con.cursor()
	cur.execute("DROP TABLE links")
	con.commit()
	con.close()

def reset_db():
	con = sqlite3.connect(db_path)
	cur = con.cursor()
	cur.execute("DROP TABLE links")
	con.commit()
	cur.execute("CREATE TABLE links(url)")
	con.commit()
	con.close()


def insert_link(url):
	con = sqlite3.connect(db_path)
	cur = con.cursor()
	cur.execute('INSERT INTO links VALUES(?);', [url])
	con.commit()
	con.close()

def delete_link(url):
	con = sqlite3.connect(db_path)
	cur = con.cursor()
	cur.execute('DELETE FROM links WHERE url=?;', [url])
	con.commit()
	con.close()

def get_all_links():
	con = sqlite3.connect(db_path)
	cur = con.cursor()
	cur.execute('SELECT * FROM links')
	result = cur.fetchall()
	con.commit()
	con.close()
	return list(map(lambda x: x[0], result))