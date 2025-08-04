from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]



@app.route('/todos', methods=['GET'])
def hello_world():
    # You can convert that variable into a json string like this
    json_text = jsonify(todos)

    # And then you can return it to the front end in the response body like this
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_todo = request.json
    print("Incoming request with the following body", request_todo)
    return 'Response for the POST todo'

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(ind):
    print("This is the position to delete:", ind)
    popped = todos.pop(ind)
    print("popped", popped)
    json_text = jsonify (todos)
    return json_text


# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)