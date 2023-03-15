# This file is testing the functions of controller.py, all functions within this file should be tested. 
# Unit tests are not testing the entire app, just this single function
# When testing you should be using a TEST_DB, to easily do this modify the db.py so it is using a new DB
# When testing on a test_db you should automatically reset the DB after testing and populate it with some data before testing

# def test_read_by_id():
#     # Arrange - Variables and values needed for the test
#     test_id = 1
#     result = None
#     expected = Order("test name", "test mocha", False, 1.23)

#     # Act - What you are testing 
#     result = controller.read_by_id(test_id)

#     # Assert - Asserting whether what you assume happens, does happen
#     assert result == expected
    
#  ----------------------------------------------------------------------
from service import *
from test_db import *

def test_addTicket(mocker):
    # Arrange
    test_data = True
    mocker.patch("test_db.addTicket", return_value = test_data)
    # assigned_to = Doyoung D
    # severity = 5
    # ticket_status = OPEN
    # title = Vending Machine item stuck
    # notes = the vending machine on floor 7 in the kitchen has a few items stuck
    # result = None
    # expected = ({assigned_to}, {severity}, {ticket_status}, {title}, {notes})
    
    # Act
    result = create_ticket('Doyoung D', 5, 'OPEN', 'Vending Machine item stuck', 'the vending machine on floor 7 in the kitchen has a few items stuck')
    
    # Assert
    assert result == 'Successfully added ticket'

def test_view_ticket():
    # Arrange
    test_id = 1
    test_data = [(1, 'time', 'Abiodun A', 5, 'OPEN', 'Locker assignment', 'Assign locker to client in office')]
    
    # Act
    result = view_ticket(test_id)
    
    # Assert
    result == test_data
    
def test_delete_all_ticket(mocker):
    # Arrange
    test_data = None
    mocker.patch("test_db.deleteAllTickets", return_value = test_data)
    
    # Act
    result = delete_all_tickets()
    
    # Assert
    assert result == test_data