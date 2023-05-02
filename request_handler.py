import json
from http.server import BaseHTTPRequestHandler, HTTPServer
# add this import to the top of the file
from urllib.parse import urlparse, parse_qs
from views import get_all_animals, get_single_animal, delete_animal, create_animal
from views import update_animal, get_all_employees, get_single_employee, create_employee
from views import update_employee, delete_employee, get_all_locations, create_location, get_single_location
from views import update_location, delete_location,  get_single_customer, get_all_customers, create_customer, update_customer
from views import get_customers_by_email, get_animal_by_location, get_employee_by_location, get_animal_by_status

# a dictionary to deal with single or all resources
method_mapper = {
    'animals' : {
        'all' : get_all_animals,
        'single' : get_single_animal
    },
    'locations' : {
        'all' : get_all_locations,
        'single' : get_single_location
    },
    'employees' : {
        'all' : get_all_employees,
        'single' : get_single_employee
    },
    'customers' : {
        'all' : get_all_customers,
        'single' : get_single_customer
    },

}


# This is a class which inherits from another class.
# For now, think of a class as a container for functions that
# work together for a common purpose. In this case, that
# common purpose is to respond to HTTP requests from a client.


class HandleRequests(BaseHTTPRequestHandler):
    '''handles the fetch methods'''

    

    # replace the parse_url function in the class
    def parse_url(self, path):
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/')  # ['', 'animals', 1]
        resource = path_params[1]

        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)

        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)

   # def parse_url(self, path):
    #    '''splitting string. If the path is "/animals/1", the resulting list will have "" at index 0, "animals" at index 1, and "1" at index 2.'''

   #     path_params = path.split("/")
   #     resource = path_params[1]
   #     id = None

        # Try to get item at index 2
   #     try:
   #         id = int(path_params[2])
   #     except IndexError:
   #         pass
   #     except ValueError:
  #          pass

  #      return (resource, id)


    def get_all_or_single(self, resource, id):
        '''method to get compile the getter functions'''
        if id is not None:
            #looking for a particular id
            response = method_mapper[resource]["single"](id)

            if response is not None:
                #meaning it exists
                self._set_headers(200)
            else:
                self._set_headers(404)
                response = ''
        else:
            self._set_headers(200)
            response = method_mapper[resource]["all"]()

        return response
    # Here's a class method

    def do_GET(self):
        '''sql fetches'''
        self._set_headers(200)

        response = {}

        # Parse URL and store entire tuple in a variable
        parsed = self.parse_url(self.path)

        # If the path does not include a query parameter, continue with the original if block
        if '?' not in self.path:
            ( resource, id ) = parsed

            if resource == "animals":
                if id is not None:
                    response = get_single_animal(id)
                else:
                    response = get_all_animals()
            elif resource == "customers":
                if id is not None:
                    response = get_single_customer(id)
                else:
                    response = get_all_customers()
            elif resource == "employees":
                if id is not None:
                    response = get_single_employee(id)
                else:
                    response = get_all_employees()
            elif resource == "locations":
                if id is not None:
                    response = get_single_location(id)
                else:
                    response = get_all_locations()

        else: # There is a ? in the path, run the query param functions
            (resource, query) = parsed

            # see if the query dictionary has an email key
            if query.get('email') and resource == 'customers':
                response = get_customers_by_email(query['email'][0])
            elif query.get('location_id') and resource == 'animals':
                response = get_animal_by_location(query['location_id'][0])
            elif query.get('location_id') and resource == 'employees':
                response = get_employee_by_location(query['location_id'][0])
            elif query.get('status') and resource == 'animals':
                response = get_animal_by_status(query['status'][0])
                
            

        self.wfile.write(json.dumps(response).encode())


   # def do_GET(self):
     #   """Handles GET requests to the server"""
        

        #response = {} #empty dictionary
        #refractor dry code
       # response = None
      #  (resource, id) = self.parse_url(self.path)
      #  response = self.get_all_or_single(resource, id)
      #  self.wfile.write(json.dumps(response).encode())

        # Set the response code to 'Ok'

        # Parse the URL and capture the tuple that is returned
       # (resource, id) = self.parse_url(self.path)

       # if resource == "animals":
         #   if id is not None:
        #        response = get_single_animal(id)

        #        if response is not None:
        #            self._set_headers(200)
        #        else:
        #            self._set_headers(404)
        #            response = {"message": "Oh no! Animal has escaped!"}

        #    else:
        #        self._set_headers(200)
         #       response = get_all_animals()

       # elif resource == "locations":
       #     if id is not None:
       #         response = get_single_location(id)

       #         if response is not None:
       #             self._set_headers(200)
        #        else:
         #           self._set_headers(404)
          #          response = {"message": "Use a valid address"}
#
 #           else:
  #              self._set_headers(200)
   #             response = get_all_locations()
#
 #       elif resource == "customers":
  ##             response = get_single_customer(id)
#
 #               if response is not None:
  #                  self._set_headers(200)
   #             else:
    #                self._set_headers(404)
     #               response = {"message": "This person does not exist."}

      #      else:
       #         self._set_headers(200)
        #        response = get_all_customers()
#
 #       elif response == "employees":
  #          if id is not None:
   #             response = get_single_employee(id)
#
 #               if response is not None:
  #                  self._set_headers(200)
   #             else:
    #                self._set_headers(404)
     #               response = {"message": "Oh no! This employee ran away"}
#
 #           else:
  #              self._set_headers(200)
   #             response = get_all_employees()
#
 #       # Send a JSON formatted string as a response
  #      self.wfile.write(json.dumps(response).encode())

    # Here's a method on the class that overrides the parent's method.
    # handles any POST request.
    def do_POST(self):
        """Handles POST requests to the server"""
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new item
        created_resource = None
        new_employee = None
        new_customer = None

        if resource == "animals":
            if "name" in post_body and "breed" in post_body and "status" in post_body:
                self._set_headers(201)
                created_resource = create_animal(post_body)
            else:
                self._set_headers(400)
                created_resource = {
                    "message": f'{"please enter a name" if "name" not in post_body else ""}{"please enter species" if "breed" not in post_body else ""}{"please enter status" if "status" not in post_body else ""}'
                }
        # Encode the new animal and send in response
            self.wfile.write(json.dumps(created_resource).encode())

        if resource == "locations":
            if "address" in post_body and "name" in post_body:
                self._set_headers(201)
                created_resource = create_location(post_body)
            else:
                self._set_headers(400)
                created_resource = {
                    "message": f'{"please enter a name" if "name" not in post_body else ""}{"please enter a location" if "address" not in post_body else ""}'}
            self.wfile.write(json.dumps(created_resource).encode())

        if resource == "customers":
            new_customer = create_customer(post_body)

            self.wfile.write(json.dumps(new_customer).encode())

        if resource == "employees":
            new_employee = create_employee(post_body)

            self.wfile.write(json.dumps(new_employee).encode())

    def do_PUT(self):
        '''update'''
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

    # Parse the URL
        (resource, id) = self.parse_url(self.path)

        success = False

        if resource == "animals":
            success = update_animal(id, post_body)
        # rest of the elif's

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())

    

    # A method that handles any PUT request.
   # def do_PUT(self):
     #   """Handles PUT requests to the server"""
      #  self._set_headers(204)
      #  content_len = int(self.headers.get('content-length', 0))
      #  post_body = self.rfile.read(content_len)
      #  post_body = json.loads(post_body)

        # Parse the URL
      #  (resource, id) = self.parse_url(self.path)

       # if resource == "animals":
      #      update_animal(id, post_body)

      #  if resource == "customers":
      #      update_customer(id, post_body)

      #  if resource == "employees":
       #     update_employee(id, post_body)

       # if resource == "locations":
       #     update_location(id, post_body)

        # Encode the new animal and send in response
       # self.wfile.write("".encode())

    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response
        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_DELETE(self):
        '''delete handler'''
        # Set a 204 response

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal
        if resource == "animals":
            self._set_headers(204)
            delete_animal(id)
            self.wfile.write(''.encode())

        if resource == "employees":
            self._set_headers(204)
            delete_employee(id)
            self.wfile.write("".encode())

        if resource == "locations":
            self._set_headers(204)
            delete_location(id)
            self.wfile.write("".encode())

        if resource == "customers":
            self._set_headers(405)
            response = {"message": "this is not allowed. Please contact admin"}
            self.wfile.write(json.dumps(response).encode())

            # delete_customer(id)
        # Encode the new animal and send in response

    # Another method! This supports requests with the OPTIONS verb.

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()


# This function is not inside the class. It is the starting
# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
