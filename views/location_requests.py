import sqlite3
import json
from .models import Location


LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike",
        "vacant": 'Yes'
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive",
        "vacant": 'No'
    }
]

def get_all_locations():
    '''single location'''
    #open connection to database
    with sqlite3.connect('kennel.sqlite3') as conn:
        #use these it's a black box
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        #write sql query to get info
        db_cursor.execute('''
        SELECT
            l.id,  
            l.name,
            l.address
        FROM location l
        ''')

        #initalize an empty list to hold on location representations
        locations = []

        #convert rows of data into python list
        dataset = db_cursor.fetchall()


        #iterate list of data returned from database
        for row in dataset:
        
            #create a location instance from the current row.
            #note database fields are specified in order of parameters defined in location class
            location = Location(row['id'], row['name'], row['address'])
            locations.append(location.__dict__)
            
    return locations

# Function with a single parameter
def get_single_location(id):
    '''single employee with sql'''
    with sqlite3.connect("kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            l.id,  
            l.name,
            l.address
        FROM location l
        WHERE l.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        location = Location(data['id'], data['name'], data['address'])

        return location.__dict__

def create_location(location):
    """post location"""
    # Get the id value of the last animal in the list
    max_id = LOCATIONS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    location["id"] = new_id

    # Add the animal dictionary to the list
    LOCATIONS.append(location)

    # Return the dictionary with `id` property added
    return location

def delete_location(id):
    """delete location"""

    location_index = -1

    for index, location in enumerate(LOCATIONS):
        if location['id'] == id:
            location_index = index
    
    if location_index >= 0:
        LOCATIONS.pop(location_index)
    

def update_location(id, new_location):
    """update location"""

    for index, location in enumerate(LOCATIONS):
        if location['id'] == id:
            LOCATIONS[index] = new_location
            break
   