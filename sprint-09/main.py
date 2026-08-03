import json
from http.server import HTTPServer, BaseHTTPRequestHandler

USERS_LIST = [
    {
        "id": 1,
        "username": "theUser",
        "firstName": "John",
        "lastName": "James",
        "email": "john@email.com",
        "password": "12345",
    }
]


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_response(self, status_code=200, body=None):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(body if body else {}).encode("utf-8"))

    def _pars_body(self):
        content_length = int(self.headers["Content-Length"])  # <--- Gets the size of data
        return json.loads(self.rfile.read(content_length).decode("utf-8"))  # <--- Gets the data itself


    def check_user_by_schema(self, new_user, method):
        '''
        Method which compare user's attributes according to schema.
        The schema depend on wether it POST method or not.
        '''
        schema_for_new_user = {
                        "id": int,
                        "username": str,
                        "firstName": str,
                        "lastName": str,
                        "email": str,
                        "password": str
                    } if method=="POST" else {
                        "username": str,
                        "firstName": str,
                        "lastName": str,
                        "email": str,
                        "password": str
                    }

        if len(new_user) != len(schema_for_new_user):
            return None

        for parameter, expected_type in schema_for_new_user.items():
            if parameter not in new_user or not isinstance(new_user[parameter], expected_type):
                return None
        else:
            return new_user


    def check_user_not_exist(self, user):
        '''
        Method which checks if user in not in USERS_LIST by id
        '''
        for existing_user in USERS_LIST:
            if existing_user["id"] == user["id"]:
                return False
        return True 


    def do_GET(self):

        path_parts = tuple(self.path.strip("/").split("/"))

        match path_parts:
            case ("reset",):
                global USERS_LIST 

                USERS_LIST = [
                    {
                        "id": 1,
                        "username": "theUser",
                        "firstName": "John",
                        "lastName": "James",
                        "email": "john@email.com",
                        "password": "12345"
                    }
                ]

                return self._set_response(200, USERS_LIST)

            case ("users",):
                return self._set_response(200, USERS_LIST)

            case ("user", user_name_to_find):
                dict_of_users = {user["username"] : user for user in USERS_LIST}

                try:
                    user = dict_of_users[user_name_to_find]
                except KeyError:
                        return self._set_response(400, {"error": "User not found"})
                else:
                    return self._set_response(200, user)

            case _:
                return self._set_response(404, {"error": "Not Found"})


    def do_POST(self):

        try:
            given_data = self._pars_body()

            if isinstance(given_data, (dict, list)):
                global USERS_LIST

                path_parts = tuple(self.path.strip("/").split("/"))

                match path_parts:
                    case ("user",):

                        new_user = self.check_user_by_schema(given_data, method="POST")

                        if new_user is not None and self.check_user_not_exist(new_user):
                            USERS_LIST.append(new_user)
                            return self._set_response(201, new_user)
                        else:
                            raise Exception

                    case ("user", "createWithList"):
                        if isinstance(given_data, list) and len(given_data) == 0:
                            raise Exception

                        for user in given_data:
                            new_user = self.check_user_by_schema(user, method="POST")

                            if new_user is not None and self.check_user_not_exist(new_user):
                                continue
                            else:
                                raise Exception
                        else:
                            USERS_LIST.extend(given_data)
                            return self._set_response(201, given_data)

                    case _ :
                        return self._set_response(404, {"error": "Route not found"})

        except Exception:
            return self._set_response(400, {})


    def do_PUT(self):

        path_parts = tuple(self.path.strip("/").split("/"))

        try:
            given_data = self._pars_body()

            if isinstance(given_data, dict):
                global USERS_LIST

                match path_parts:
                    case ("user", user_id):

                        update_user = self.check_user_by_schema(given_data, method="PUT")

                        if update_user is None:
                            raise Exception

                        for user in USERS_LIST:
                            if user["id"] == int(user_id):
                                user.update(given_data)
                                return self._set_response(200, user)
                            
                        return self._set_response(404, {"error": "User not found"})

                    case _ :
                        return self._set_response(404, {"error": "Route not found"})

        except Exception:
            return self._set_response(400, {"error": "not valid request data"})


    def do_DELETE(self):

        path_parts = tuple(self.path.strip("/").split("/"))

        try:
            global USERS_LIST

            match path_parts:
                case ("user", user_id):
                    user_to_delete = None

                    for i in range(len(USERS_LIST)):
                        user = USERS_LIST[i]

                        if user["id"] == int(user_id):
                            user_to_delete = i
                            break

                    if user_to_delete is not None:
                        del USERS_LIST[user_to_delete]
                        return self._set_response(200, {})
                    else:
                        return self._set_response(404, {"error": "User not found"})

                case _ :
                    return self._set_response(404, {"error": "Route not found"})

        except Exception:
            return self._set_response(400, {"error": "not valid request data"})


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, host="localhost", port=8000):
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
