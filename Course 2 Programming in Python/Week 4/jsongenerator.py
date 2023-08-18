import json
from employee import details, employee_name, age, title

def create_dict(name, age, title):
    employee_dict = {}
    employee_dict['first_name'] = str(name)
    employee_dict['age'] = int(age)
    employee_dict['title'] = str(title)
    return employee_dict
    raise NotImplementedError()

def write_json_to_file(json_obj, output_file):
    with open(output_file, mode='w') as file:
        newfile = file.write(json_obj)
    return newfile
    raise NotImplementedError()

def main():
    details()
    employee_dict = create_dict(employee_name, age, title)
    print("employee_dict: " + str(employee_dict))
    json_object = json.dumps(employee_dict)
    print("json_object: " + str(json_object))
    write_json_to_file(json_object, "employee.json")

if __name__ == "__main__":
    main()
