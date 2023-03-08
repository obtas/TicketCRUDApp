import database as db

def create_ticket(assigned_to, severity, ticket_status, title, notes):
    new_ticket = db.addTicket()
    return new_ticket

def view_ticket(id):
    view_ticket = db.viewTicket(id)
    return view_ticket

def view_all_tickets():
    all_orders = db.viewAllTickets()
    return all_orders

def update_ticket(id, table_title, value):
    update = db.updateTicket
    return update

def delete_ticket(id):
    delete_a_ticket = db.deleteTicket(id)
    return delete_a_ticket

def delete_all_tickets():
    delete_all = db.deleteAllTickets()
    return delete_all

def commit_changes():
    db.conn.commit()

