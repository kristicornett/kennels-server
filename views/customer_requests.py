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

def get_all_customers():
    """gets customers"""
    return CUSTOMERS

def get_single_customer(id):
    """gets single customer"""
    requested_customer = None
    for customer in CUSTOMERS:
        if customer['id'] == id:
            requested_customer = customer

    return requested_customer


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


