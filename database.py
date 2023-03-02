import sqlite3 as sql

# Connect to database
conn = sql.connect("ticket_db")

# Cursor object that sends commands to SQL
cursor = conn.cursor()

print("Database created and Successfully Connected to SQLite")

# close the connection
# conn.close()

def commitChanges():
    conn.commit()
    
def runQuery(query):
    data = cursor.execute(query).fetchall()
    return data
    
def setupTable():
    sql_file = open("tickets.sql")
    sql_string = sql_file.read()
    cursor.executescript(sql_string)
    print("Database table has been successfully set up")
    # commitChanges()
    # conn.close()

def addTicket(assigned_to, severity, ticket_status, title, notes):
    query = f"INSERT INTO ticket (assigned_to, severity, ticket_status, title, notes) VALUES ('{assigned_to}', '{severity}', '{ticket_status}', '{title}', '{notes}')"
    runQuery(query)
    commitChanges()
    print("Successfully added ticket")
    return True
    
def viewTicket(id):  
    view_ticket = f"SELECT * FROM ticket WHERE ticket_id = {id}"
    print(runQuery(view_ticket))
    
def viewAllTickets():
    query = "SELECT * FROM ticket"
    print(runQuery(query))
    
def updateTicket(id, table_title, value):
    update_query = f"UPDATE ticket SET '{table_title}' = '{value}' WHERE ticket_id = '{id}'"
    runQuery(update_query)
    commitChanges()
    print("Successfully updated ticket")
    return True
    
def deleteTicket(id):
    delete_query= f"DELETE FROM ticket WHERE ticket_id = {id}"
    runQuery(delete_query)
    commitChanges()
    print("Successfully deleted ticket")
    return True
    
def deleteAllTickets():
    delete_all_query = f"DELETE FROM ticket"
    runQuery(delete_all_query)
    commitChanges()
    print("Successfully deleted all tickets")
    return True
    
# setupTable() 
# print("-" * 50)  
# print(runQuery("SELECT * FROM ticket")) 
# print("-" * 50)
# # addTicket("Sam Samson", 5, "OPEN", "Dock", "New docking stations required in regional services")
# print("-" * 50)
# # print(viewAllTickets())
# print("-" * 50)
# viewAllTickets()
# print("-" * 50)
# viewTicket(1)
# # print("-" * 50)
# deleteAllTickets()
# viewAllTickets()
# print("-" * 50)
# setupTable()

