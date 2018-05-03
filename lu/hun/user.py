import sqlite3 as sql
import crypt

conn = sql.connect('seenit.db')
c = conn.cursor()
salt = '2y'

# register-insert new user
def insert(id, name, email, pwd):
    h_pwd = crypt.crypt(pwd,salt)
    query = "INSERT INTO user (u_id, u_name, pwd, email) VALUES (" + str(id) + ",'" + name + "','" + h_pwd + "','" + email + "')"
    # print (query)
    with conn:
        try:
            c.execute(query)
            print ("insert successfully")
            conn.commit()
        except:
            conn.rollback()
            print ("insert error")

def read_one(u_id):
    query = "SELECT * FROM user WHERE u_id=" + str(u_id)
    with conn: 
        try:
            c.execute(query)
            users = c.fetchall()
            user_info = users[0]
            print ("User Info read successfully")
            return user_info 
        except:
            print("User Info read error")   

# login-get user id with name and password input
def login(name, pwd):
    h_pwd = crypt.crypt(pwd,salt)
    query = "SELECT u_id FROM user WHERE u_name='" + name + "'AND pwd='" + h_pwd + "'"
    with conn: 
        try:
            c.execute(query)
            users = c.fetchall()
            _id = users[0][0]
            print ("login successfully")
            return _id 
        except:
            print("login error")        

# admin delete account
def delete(id):
    query = "DELETE FROM user WHERE u_id=" + str(id)
    # print (query)
    with conn:
        try:
            c.execute(query)
            print ("delete successfully")
            conn.commit()
        except:
            conn.rollback()
            print ("delete error")

# get all users
def read_all():
    with conn:
        try:
            c.execute("SELECT * FROM user ")
            data = c.fetchall()
            formatted_row = '{:<12} {:<12} {:<20} {:<12}'
            print(formatted_row.format("u_id", "u_name", "password", "email"))
            print ("-" * 40)
            for Row in data:
                print(formatted_row.format(*Row))
        except:
            print "read error"

# update account info
def update(id, name, pwd, email):
    h_pwd = crypt.crypt(pwd,salt)
    query = "UPDATE user SET u_name='" + name + "', pwd='" + h_pwd + "', email='" + email + "' WHERE u_id=" + str(id)
    print (query)
    with conn:
        try:
            c.execute(query)
            print ("update successfully")
            conn.commit()
        except:
            conn.rollback()
            print ("update error")

# insert(7,'b','b@email')



