from flask import Flask, render_template, request, jsonify
from DAO import populationDAO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/firstPageTest.html')

@app.route('/api/population', methods=['POST'])
def create_population():
    data = request.get_json()
    values = (data['id'], data['census_Year'], data['location'], data['marital_Status'], data['gender'], data['population'])
    new_id = populationDAO.create(values)
    return jsonify({'id': new_id})

@app.route('/api/population', methods=['GET'])
def get_all_population():
    result = populationDAO.getAll()
    return jsonify(result)

@app.route('/api/population/<int:id>', methods=['GET'])
def get_population_by_id(id):
    result = populationDAO.findByID(id)
    return jsonify(result)

@app.route('/api/population/<int:id>', methods=['PUT'])
def update_population(id):
    data = request.get_json()
    values = (data['id'], data['census_Year'], data['location'], data['marital_Status'], data['gender'], data['population'], id)
    populationDAO.update(values)
    return jsonify({'message': 'Record updated successfully'})

@app.route('/api/population/<int:id>', methods=['DELETE'])
def delete_population(id):
    populationDAO.delete(id)
    return jsonify({'message': 'Record deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
