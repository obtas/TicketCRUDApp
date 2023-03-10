import service as s
import database as db
import sys

def start_app():
    print(menu)
    exit = False
    while not exit:
        choice = input("Please select a choice: ")
        if choice == "1":
            print(create_a_ticket())
        elif choice == "2":
            print(view_a_ticket())
        elif choice == "3":
            print(view_all_tickets())
        elif choice == "4":
            print(update_ticket())
        elif choice == "5":
            print(delete_ticket())
        elif choice == "6":
            print(delete_all_tickets())
        elif choice == "7":
            sys.exit("User has quit ticket system")    
        else:
            exit = True
            db.commitChanges()
            
def create_a_ticket():
    assigned_to = input("Who is this ticket assigned to?: ")
    severity = input("What is the severity of the ticket? (1-5): ")
    ticket_status = input("What is the status of the ticket?: ")
    title = input("Please give a title for the ticket (or leave blank): ")
    notes = input("Enter any notes (or leave blank): ")
    s.create_ticket(assigned_to, severity, ticket_status, title, notes)
    # print("Ticket created")
    
def view_a_ticket():
    ticket_id = input("Please enter the ID of the ticket you would like to view: ")
    s.view_ticket(ticket_id)
    
def view_all_tickets():
    s.view_all_tickets()

def update_ticket():
    ticket_id = input("What is the ID of the ticket you would like to update?: ")
    column_to_update = input(" 1. Assigned to \n 2. Severity \n 3. Status \n 4. Title \n 5. Notes \n 6. Quit \n\n")
    if column_to_update == "6":
        start_app()
    elif column_to_update == "1":
        column_to_update = "assigned_to"
    elif column_to_update == "2":
        column_to_update = "severity"
    elif column_to_update == "3":
        column_to_update = "ticket_status"
    elif column_to_update == "4":
        column_to_update = "title"
    else:
        column_to_update == "5"
        column_to_update = "Notes"
    # table_title = input("Which item of the ticket would you like to update?: ")
    updated_value = input("Please enter the updated value: ")
    s.update_ticket(ticket_id, column_to_update, updated_value)
    
def delete_ticket():
    ticket_id = input("Please enter the ID of the ticket you would like to delete: ")
    s.delete_ticket(ticket_id)  

def delete_all_tickets():
    s.delete_all_tickets()
    
menu = """
    Welcome to the ticketing service, what would you like to do? 
    1. Create a ticket
    2. Read a ticket
    3. Read all tickets
    4. Update a ticket
    5. Delete a ticket
    6. Delete all tickets
    7. Quit
    """

start_app()