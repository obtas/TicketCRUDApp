import service as s

def start_app():
    print(menu)
    exit = False
    while not exit:
        choice = input("Please select a choice: ")
        if choice == "1":
            print(create_a_ticket())
        elif choice == "2":
            print(readOneOrder())
        elif choice == "3":
            print(readAllOrders())
        elif choice == "4":
            print(updateAnOrder())
        elif choice == "5":
            print(deleteAnOrder())
        elif choice == "6":
            print(deleteAllOrders())
        else:
            exit = True
            db.commitChanges()
            
def create_a_ticket():
    
    
def view_a_ticket():
    
    
def view_all_tickets():
    

def update_ticket():
    
def delete_ticket():
    

def delete_all_tickets():
    
    
menu = """
    Welcome to the ticketing service, what would you like to do? 
    1. Create a ticket
    2. Read a ticket
    3. Read all tickets
    4. Update a ticket
    5. Delete a ticket
    6. Delete all tickets
    """

startApp()