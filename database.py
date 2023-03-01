import sqlite3 as sql

# Connect to database
conn = sql.connect("tickets_db")

# Cursor object that sends commands to SQL
cursor = conn.cursor()

print("Database created and Successfully Connected to SQLite")

# close the connection
# conn.close()

def commitChanges():
    conn.commit()
    
def runQuery(query):
    data = cursor.execute(query).fetchall()
    
def setupTable():
    sql_file = open("tickets.sql")
    sql_string = sql_file.read()
    cursor.executescript(sql_string)
    print("Database table has been successfully set up")
    commitChanges()
    conn.close()
    
def runQuery(query):
    data = cursor.execute(query).fetchall()
    return data

def addTicket(assigned_to, severity, ticket_status, title, notes):
    query = f"INSERT INTO ticket (assigned_to, severity, ticket_status, title, notes) VALUES ('{assigned_to}', '{severity}', '{ticket_status}', '{title}', '{notes}');"
    
def viewTicket(id):  
    view_ticket = f"SELECT * FROM ticket WHERE ticket_id = {id}"
    
def viewAllTickets():
    query = "SELECT * FROM ticket"
    
def updateTicket(id, table_title, value):
    update_query = f"UPDATE ticket SET {table_title} = {value} WHERE ticket_id = {id}"
    
def deleteTicket(id):
    delete_query= f"DELETE FROM ticket WHERE order_id = {id}"
    
def deleteAllTickets():
    delete_all_query = f"DELETE FROM ticket"
      
setupTable()    