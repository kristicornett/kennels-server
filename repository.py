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
CUSTOMERS = [
    {
        "id": 1,
        "name": "Ryan Tanay",
        "returning": "No"
    },
    {
        "id": 2,
        "name": "Kristi Cornett",
        "returning": "Yes"
    },
    {
        "id": 3,
        "name": "Beth Ellis",
        "returning": "No"
    },
    {
        "id": 4,
        "name": "Anna Corbin",
        "returning": "No"
    }
]
EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis",
        "trained": "No"
    },
    {
        "id": 2,
        "name": "Beth Ellis",
        "trained": "Yes"
    }
]
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

def all(data_type=None):
     if data_type is None:
          all_data = {}
          all_data['animals'] = ANIMALS
          all_data['customers'] = CUSTOMERS
          all_data['employees'] = EMPLOYEES
          all_data['locations'] = LOCATIONS
          return all_data
     elif data_type == 'animals':
          return ANIMALS
     elif data_type == 'customer':
          return CUSTOMERS
     elif data_type == 'employees':
          return EMPLOYEES
     elif data_type == 'locations':
          return LOCATIONS
     else:
          raise ValueError('Invalid data type specified')

all_data = all()
animal_data = all('animals')
customer_data = all('customers')
employee_data = all('employees')
location_data = all('locations')

def retrieve(data_type, id):
    '''retrieve single'''
    requested_data = {}
    requested_object = None
    
    if data_type == 'animals':
         requested_data = ANIMALS
    elif data_type == 'customers':
          requested_data = CUSTOMERS

    for data in requested_data:
         if data['id]'] == id:
              requested_object = data.copy()
    return requested_object

def update():
    pass

def delete():
    pass

def create():
    pass