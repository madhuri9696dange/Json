# Python to json


# How to retrieve values from json string in python ......demo -

try:
    # importing package json
    import json
    #json

# JSON string:
    json_var = '{ "EmpName":"Tom", "EmpAge":29, "EmpDesignation":"Senior Developer"}'

# parse result :
    result = json.loads(json_var)

    print(result)

    print(type(result))

    print(f"Employee Name = {result['EmpName']}")
    print(f"Employee Age = {result['EmpAge']}")
    print(f"Employee Designation = {result['EmpDesignation']}")


except Exception as e:
    print(f"Error Occurred = {e}")
