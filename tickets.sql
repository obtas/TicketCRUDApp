-- Create ticket database
-- Ticket ID, assigned to, severity, ticket status, title, notes

CREATE TABLE IF NOT EXISTS ticket(
    ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_time TEXT,
    assigned_to VARCHAR(20) NOT NULL,
    severity INTEGER NOT NULL,
    ticket_status VARCHAR(8) NOT NULL,
    title VARCHAR NULL,
    notes VARCHAR(MAX) NULL
);

INSERT INTO ticket (ticket_id, date_time, assigned_to, severity, ticket_status, title, notes) VALUES (
    'Abiodun A', '5', 'OPEN', 'Locker assignment', 'Assign locker to client in office')

INSERT INTO ticket (ticket_id, date_time, assigned_to, severity, ticket_status, title, notes) VALUES (
    'Beth B', '5', 'RESOLVED', 'Vending Machine', 'Refund processed')

INSERT INTO ticket (ticket_id, date_time, assigned_to, severity, ticket_status, title, notes) VALUES (
    'Carl C', '3', 'CLOSED', 'Bathroom on floor 2')

INSERT INTO ticket (ticket_id, date_time, assigned_to, severity, ticket_status, title, notes) VALUES (
    'Daniel D', '5', 'OPEN', 'Kitchen on floor 5', 'Coffee machine screen broken')