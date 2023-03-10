import database as db

def create_ticket(assigned_to, severity, ticket_status, title, notes):
    new_ticket = db.addTicket(assigned_to, severity, ticket_status, title, notes)
    return new_ticket

def view_ticket(id):
    view_ticket = db.viewTicket(id)
    return view_ticket

def view_all_tickets():
    all_tickets = db.viewAllTickets()
    return all_tickets

def update_ticket(ticket_id, column_to_update, updated_value):
    update = db.updateTicket(ticket_id, column_to_update, updated_value)
    return update

def delete_ticket(id):
    delete_a_ticket = db.deleteTicket(id)
    return delete_a_ticket

def delete_all_tickets():
    delete_all = db.deleteAllTickets()
    return delete_all

def commit_changes():
    db.conn.commit()

