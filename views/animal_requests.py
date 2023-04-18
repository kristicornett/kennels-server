import sqlite3
import json
from .models import Animal, Location, Customer
from .location_requests import get_single_location
from .customer_requests import get_single_customer


ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4,
        "status": "Admitted"
    },
    {
        "id": 2,
        "name": "Roman",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2,
        "status": "Admitted"
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1,
        "status": "Admitted"
    }
]


def get_all_animals():
    '''sql fetch'''
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id,
            l.name location_name,
            l.address location_address,
            c.name customer_name,
            c.address customer_address,
            c.email customer_email
        FROM Animal a
        JOIN Location l
            ON l.id = a.location_id
        JOIN Customer c
            ON c.id = a.customer_id
        """)

        # Initialize an empty list to hold all animal representations
        animals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
           

    # Create an animal instance from the current row
            animal = Animal(row['id'], row['name'], row['breed'], row['status'],
                    row['location_id'], row['customer_id'])

    # Create a Location instance from the current row
            location = Location(row['id'], row['location_name'], row['location_address'])
            customer = Customer(row['id'], row['customer_name'], row['customer_address'],row['customer_email'])
    # Add the dictionary representation of the location to the animal
            animal.location = location.__dict__
            animal.customer = customer.__dict__
    # Add the dictionary representation of the animal to the list
            animals.append(animal.__dict__)
    return animals

# Function with a single parameter
#def get_single_animal(id):
  #  """get single animal"""
    # Variable to hold the found animal, if it exists
    #requested_animal = None
   

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    #for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        #if animal["id"] == id:
           # requested_animal = animal.copy()
           # matching_location = get_single_location(requested_animal['locationId'])
           # requested_animal['location'] = matching_location

            #matching_customer = get_single_customer(requested_animal['customerId'])
            #requested_animal['customer'] = matching_customer
        
        #animal.pop("locationId", None)
        #animal.pop("customerId", None)

    #return requested_animal

def get_single_animal(id):
    '''single animal with sql'''
    with sqlite3.connect("kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        animal = Animal(data['id'], data['name'], data['breed'],
                            data['status'], data['location_id'],
                            data['customer_id'])

        return animal.__dict__

def create_animal(animal):
    """create animal"""
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with `id` property added
    return animal

#def delete_animal(id):
#    """delete animal"""
    # Initial -1 value for animal index, in case one isn't found
 #   animal_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
#    for index, animal in enumerate(ANIMALS):
#        if animal["id"] == id:
            # Found the animal. Store the current index.
#            animal_index = index

    # If the animal was found, use pop(int) to remove it from list
#    if animal_index >= 0:
 #       ANIMALS.pop(animal_index)
    
#def update_animal(id, new_animal):
  #  """update animal"""
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
   # for index, animal in enumerate(ANIMALS):
   #     if animal["id"] == id:
            # Found the animal. Update the value.
    #        ANIMALS[index] = new_animal
    #        break
def update_animal(id, new_animal):
    '''update animal'''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Animal
            SET
                name = ?,
                breed = ?,
                status = ?,
                location_id = ?,
                customer_id = ?
        WHERE id = ?
        """, (new_animal['name'], new_animal['breed'],
              new_animal['status'], new_animal['locationId'],
              new_animal['customerId'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True


def get_animal_by_location(location_id):
    '''ANIMAL BY LOCATION'''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        from animal a
        WHERE a.location_id = ?
        """, ( location_id, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])

            animals.append(animal.__dict__)

    return animals

def get_animal_by_status(status):
    '''animal by status'''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        from animal a
        WHERE a.status = ?
        """, ( status, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])

            animals.append(animal.__dict__)

    return animals

def delete_animal(id):
    '''delete animal'''
    with sqlite3.connect('./kennel.sqlite3') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM animal
        WHERE id = ?
        """, (id, ))

#class Animal():
  #  """First class for Kennels-server"""
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
   # def __init__(self, id, name, breed, status, location_id, customer_id):
       # self.id = id
        #self.name = name
        #self.breed = breed
       # self.status = status
        #self.location_id = location_id
        #self.customer_id = customer_id
    
#new_animal = Animal(1, "Snickers", "Dog", "Recreation", 1, 4)
