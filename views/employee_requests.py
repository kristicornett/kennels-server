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

def get_all_employees():
    """gets employees"""
    return EMPLOYEES

# Function with a single parameter
def get_single_employee(id):
    """gets single employee"""
    requested_employee = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    """post location"""
    # Get the id value of the last animal in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    employee["id"] = new_id

    # Add the animal dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee

def delete_employee(id):
    """delete employee"""
    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee['id'] == id:
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)


def update_employee(id, new_employee):
    """update employee"""
    for index, employee in enumerate(EMPLOYEES):
        if employee['id'] == id:
            EMPLOYEES[index] = new_employee
            break


