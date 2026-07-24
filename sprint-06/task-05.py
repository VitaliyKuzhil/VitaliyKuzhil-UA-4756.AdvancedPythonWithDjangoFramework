import json
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def parse_user(output_file, *input_files):
    unique_users = []
    seen_names = set()
    
    for file_name in input_files:
        try:
            with open(file_name, 'r') as f:
                users = json.load(f)
                for user in users:
                    if  'name' in user:
                        name = user['name']
                        if name not in seen_names:
                            seen_names.add(name)
                            unique_users.append(user)
        except FileNotFoundError:
            logging.error(f'File {file_name} doesn\'t exist')
            
    with open(output_file, 'w') as f:
        json.dump(unique_users, f, indent=4)
