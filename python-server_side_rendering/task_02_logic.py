from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/items')
def items():
    # Open and read the JSON file
    with open('items.json', 'r') as f:
        data = json.load(f)

    # Get the list of items from the JSON data
    items_list = data.get('items', [])

    # Pass the items list to the template
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True)
