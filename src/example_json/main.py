'''
example from:
https://www.w3schools.com/python/python_json.asp
'''

import json

# compare two proteins
def main():
        # a Python object (dict):
        x = {
          "name": "John",
          "age": 30,
          "city": "New York"
        }

        # convert into JSON:
        y = json.dumps(x)

        # the result is a JSON string:
        print(y)

if __name__ == '__main__':
	main()
