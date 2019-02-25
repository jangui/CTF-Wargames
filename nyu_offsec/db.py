import MySQLdb as db

conn = db.connect("localhost", "root", "wccxwccx", "test")
c = conn.cursor()

email = "jaime@mail.com"
password = "lame_password"

c.execute("SELECT id, email, password FROM users WHERE email=%r AND password=%r", (email, password))
conn.commit()

rows = c.fetchall()
for row in rows:
    print row


c.execute("SELECT id, email, password FROM users UNION SELECT column_name, 1, 1 from information_schema.columns WHERE table_name = 'users' AND column_name LIKE 'email';")
conn.commit()

rows = c.fetchall()
for row in rows:
    print row
