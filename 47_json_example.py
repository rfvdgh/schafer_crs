''' JavaScript Object Notation '''
import json

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "555-555-5555",
            "emails": ["johnsmith@gmail.com", "john.smith@work.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "444-444-4444",
            "emails": null,
            "has_license": true
        }
    ]
}
'''
data = json.loads(people_string)

for person in data['people']:
    del person['phone']

# indents 2 per level
new_string = json.dumps(data, indent=2, sort_keys=True)

print(new_string)
