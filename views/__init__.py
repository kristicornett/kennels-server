import json
from .animal_requests import get_all_animals, update_animal, get_animal_by_status
from .animal_requests import get_single_animal, delete_animal, get_animal_by_location, create_animal
from .location_requests import get_all_locations, get_single_location, create_location
from .location_requests import delete_location, update_location
from .employee_requests import get_all_employees, get_single_employee, create_employee
from .employee_requests import delete_employee, update_employee, get_employee_by_location
from .customer_requests import get_all_customers, get_single_customer, create_customer
from .customer_requests import delete_customer, update_customer, get_customers_by_email
