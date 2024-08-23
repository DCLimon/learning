# +---------+
# | Imports |
# +---------+

import json
from urllib.request import urlopen


# +---------------------------------------+
# | Read .json string in as Python object |
# +---------------------------------------+

# Valid JSON string. Note the following:
# (1) Actual JSON string uses double-quotes, not single-quotes
# (2) true & false are lower-case
# (3) null instead of None or empty list
people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusmail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

# Convert JSON string to Python object
data = json.loads(people_string)
print(data)  # true/false -> True/False, null -> None
print(type(data))  # Python loads JSON as a dict

# Note the following:
# - data var is a dict w/ 1 key ('people')
# - data['people'] is a list of len=2
# - data['people'] list consists of 2 dicts (corresponding to 1 person's info)
print(type(data['people']))  # list


# +---------------------------+
# | Access JSON Python object |
# +---------------------------+

# Print each person's info dict separately
for person in data['people']:
    print(person)

# Print each person's info by accessing their info dict
for person in data['people']:
    print(person['name'])

# Get list of all people's names
print([person['name'] for person in data['people']])

# Get list of all people's last names
print([person['name'].split(' ')[-1] for person in data['people']])

# Get list of phone #s of all people w/ last name Doe
print(
    [
        person['phone'] for person in data['people']
        if person['name'].split(' ')[-1] == 'Doe'
    ]
)


# +--------------------------------------+
# | Dumping Python object to JSON string |
# +--------------------------------------+

# Remove phone # from each person
for person in data['people']:
    del person['phone']  # NOTE: this permanently alters data object

# Convert object back to a JSON string
scrubbed_string = json.dumps(data)
print(scrubbed_string)

# Convert to more readable JSON string
scrubbed_string = json.dumps(
    data,  # Source Python object
    indent=2,  # Number of spaces to indent each level
    sort_keys=True  # Make dict keys alphabetical
)
print(scrubbed_string)


# +-----------------+
# | Load .json file |
# +-----------------+

# json.loads() & json.dumps() loads from/dumps to a JSON-compatible STRING
# json.load() & json.dump() loads from/dumps to a .json FILE

# .json of all US states, 2-letter abbrevs, & all area codes in each state
with open('states.json') as f:
    data = json.load(f)

# Print list of (name, abbrev) tuples for each state. This borders on
# confusingly complex list comprehension
print(
    [
        (state['name'], state['abbreviation']) for state in data['states']
    ]
)

# Print state & abbreviations for each state
for state in data['states']:
    print(f"{state['name']} ({state['abbreviation']})")

# Remove area codes from the Python object
for state in data['states']:
    del state['area_codes']

# Write Python object back to .json file, w/ readable indenting
with open('states_after.json', 'w') as f:
    json.dump(data, f, indent=2)


# +----------------------+
# | Real-world API .json |
# +----------------------+

# Will use Yahoo Finance API w/ ForEx Exchange Ratios.
# NOTE: This page is now shut down. Replace by yfinance module

# Issue API call, which returns a JSON-compatible string
with urlopen('https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/'
             'quote?format=json') as response:
    source = response.read()
    # data = json.loads(response.read())  # One step API call to obj

# Convert string to Python object
data = json.loads(source)

# Check out the import in human-readable format
print(json.dumps(data, indent=2))
