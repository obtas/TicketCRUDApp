import sqlite3 as sql
from tabulate import tabulate
# from database import viewAllTickets2

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
    single_ticket = runQuery(view_ticket)
    table = tabulate(single_ticket, headers=["Ticket ID", "Date and Time of Ticket Creation", "Assigned to", "Severity", "Status", "Title", "Notes"], tablefmt="grid", stralign="center")
    print(table)
   
def viewAllTickets():
    query = "SELECT * FROM ticket"
    ticket_list = runQuery(query)
    table = tabulate(ticket_list, headers=["Ticket ID", "Date and Time of Ticket Creation", "Assigned to", "Severity", "Status", "Title", "Notes"], tablefmt="grid", stralign="center")
    print(table)
    
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
viewTicket(26)
# # print("-" * 50)
# deleteAllTickets()
# viewAllTickets()
# print("-" * 50)
# setupTable()
