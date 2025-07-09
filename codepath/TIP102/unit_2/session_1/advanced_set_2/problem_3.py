"""
Problem 3: Ticket Sales

A dictionary ticket_sales is used to map ticket type to number of tickets sold. Return the total number of tickets of all types sold.

def total_sales(ticket_sales):
    pass

Example Usage:

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))

Example Output:

4500
"""

def total_sales(ticket_sales):
    sum = 0
    for x in ticket_sales:
        sum += ticket_sales[x]
    return sum

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))