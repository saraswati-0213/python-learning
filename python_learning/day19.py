import sqlite3
con=sqlite3.connect(":memory:")
cur=sqlite3.connect("user.db")
# con=sqlite3.connect("students.db")
# cur=con.cursor()
# cur.execute("""create table if not exists students(id integer primary key,name text not null,marks real)""")
# cur.execute("""insert into students(name,marks) values ('rahul',85)""")
# cur.execute("""create table if not exists users(name text not null)""")
# cur.executemany("""insert into users(name) values (?)""",[("A",),
#             ("B",),("C",)])
# cur.execute("select*from users")
# print(cur.fetchall())
# # a=cur.fetchone()
# # b=cur.fetchone()

# con.commit()
# # cur.execute("select name from students")
# # print(cur.fetchone())
# con.close()