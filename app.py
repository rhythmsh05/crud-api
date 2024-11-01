## API Endpoints
# GET /students**: Retrieve all students
# GET /students/{id}**: Retrieve student by ID
# POST /students**: Add a new student
# PUT /students/{id}**: Update a student by ID
# DELETE /students/{id}**: Delete a student by ID




from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample in-memory database (dictionary)
students = {}

# Create a new student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    student_id = data.get("ID")
    if student_id in students:
        abort(400, "Student ID already exists.")
    
    students[student_id] = {
        "Name": data.get("Name"),
        "Grade": data.get("Grade"),
        "Email": data.get("Email")
    }
    return jsonify({"message": "Student added successfully"}), 201

# Retrieve all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# Retrieve a student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = students.get(id)
    if student is None:
        abort(404, "Student not found.")
    return jsonify(student)

# Update a student by ID
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    if id not in students:
        abort(404, "Student not found.")
    
    data = request.get_json()
    students[id] = {
        "Name": data.get("Name"),
        "Grade": data.get("Grade"),
        "Email": data.get("Email")
    }
    return jsonify({"message": "Student updated successfully"})

# Delete a student by ID
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    if id not in students:
        abort(404, "Student not found.")
    
    del students[id]
    return jsonify({"message": "Student deleted successfully"}), 204

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
