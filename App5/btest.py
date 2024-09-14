from bottle import route, run, request
import json
import os

@route('/', method='GET')
def index():
    return '''
        <form action="/save" method="post">
            <input type="text" name="data" required>
            <input type="submit" value="Save">
        </form>
    '''

@route('/save', method='POST')
def save():
    data = request.forms.get('data')
    
    filename = 'data.json'
    if not os.path.exists(filename):
        # If file doesn't exist, create it with initial data
        initial_data = ["Initial entry"]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(initial_data, f, ensure_ascii=False, indent=2)
    
    try:
        # Read existing data
        with open(filename, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
    except json.JSONDecodeError:
        # If file is empty or contains invalid JSON, start with an empty list
        existing_data = []
    
    # Append new data
    existing_data.append(data)
    
    # Write updated data
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)
    
    return f"Data '{data}' saved successfully!"

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)