import os
import re
import pyperclip

with open('jsonobject.txt', 'r') as file:
    string_data = file.read()


def format_json(json_string):
    pattern = r'([\{\,]\s*)(\w+?)\s*:'
    
    def add_quotes(match):
        return f'{match.group(1)}"{match.group(2)}":'
    
    formatted_json = re.sub(pattern, add_quotes, json_string)
    
    formatted_json = formatted_json.replace("'", '"')
    
    return formatted_json

formatted_json = format_json(string_data)

pyperclip.copy(formatted_json) # optional to copy on clipboard

#if os.path.isfile('formattedjson.txt'):
 #   print("formatted.txt file already exists. Replacing its contents.")

with open('formattedjson.json', 'w') as output_file:
    output_file.write(formatted_json)

print(formatted_json)
