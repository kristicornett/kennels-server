import sqlite3
import json
from .models import Customer

CUSTOMERS = [
    {
        "id": 1,
        "name": "Ryan Tanay",
        "address": '201 Created Streets',
        "email": 'r@tanay.com',
        "password": 'password'

    },
    {
        "id": 2,
        "name": "Kristi Cornett",
        "address": '555 no idea',
        "email": 'k@cornett.com',
        "password": 'password'
    },
    {
        "id": 3,
        "name": "Beth Ellis",
        "address": '432 figure it out ln',
        "email": 'b@ellis.com',
        "password": 'password'
    },
    {
        "id": 4,
        "name": "Anna Corbin",
        "address": '333 we got this',
        "email": 'a@corbin.com',
        "password": 'password'
    },
   
]
def get_all_customers():
    '''single customer'''
    #Open a connection to the database
    with sqlite3.connect('kennel.sqlite3') as conn:
        #use these it's a black box
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        #write sql query to get info you want
        db_cursor.execute('''
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c
        ''')
        #initialize an empty list to hold on customer representations
        customers = []

        #convert rows of data into a python list
        dataset = db_cursor.fetchall()

        #iterate list of data returned from database
        for row in dataset:
            #create a customer instance from the current row.
            #note database fields are specified in order of parameters defined in customer class
            customer = Customer(row['id'], row['name'], row['address'], row['email'], row['password'])
            customers.append(customer.__dict__)
    return customers



def get_single_customer(id):
    '''single customer with sql'''
    with sqlite3.connect("kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c
        WHERE c.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        customer = Customer(data['id'], data['name'], data['address'], data['email'], data['password'])

        return customer.__dict__
    
def get_customers_by_email(email):
    '''customer by email'''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return customers




def get_customers_by_name(name):

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.name = ?
        """, ( name, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return customers



def create_customer(customer):
    """create customer"""
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer

def delete_customer(id):
    """delete customer"""

    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer('id') == id:
            customer_index = index

        if customer_index >= 0:
            CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    """update customer"""
    for index, customer in enumerate(CUSTOMERS):
        if customer['id'] == id:
            CUSTOMERS[index] = new_customer
            break


