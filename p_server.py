from flask import Flask, jsonify, request, abort, render_template, session, url_for, g, redirect

from DAO import populationDAO 

app = Flask(__name__, static_url_path='', static_folder='staticPages', template_folder="webPages")

@app.route('/')
def initial():
    return render_template('/firstpage.html')


@app.route('/')
def getAll():
    return jsonify(populationDAO.getAll())

# get all data on to test page
@app.route('/test')
def getAll2():
    return jsonify(populationDAO.getAll())

# find by id
@app.route('/test/<int:id>')
def findbyid(id):
    return jsonify(populationDAO.findByID(id))

# create
@app.route('/test', methods = ['POST'])
def create():
    census = {
    "id": request.json['id'], 
    "census_Year": request.json["census_Year"], 
    "location": request.json["location"],
    "marital_Status": request.json["marital_Status"],
    "gender": request.json["marital_Status"],
    "population": request.json["population"],
    }
    values = (census["id"],census["census_Year"],census["location"],census["marital_Status"],census["marital_Status"],census["population"])
    new_data = populationDAO.create(values)
    census["id"] = new_data
    return request.jsonify(values)


# update
@app.route('/test/<int:id>', methods = ['PUT'])
def update(id):
    return jsonify(populationDAO.update(id))

# delete
@app.route('/test/<int:id>', methods = ['DELETE'])
def delete(id):
    return "served by delete by id with id" + str(id)







#@app.route('/', methods = ['POST'])


#def create():
#    
#    if not request.json:
#        abort(400)
#    census = {
#    "id": request.json['id'], 
#    "census_Year": request.json["census_Year"], 
#    "location": request.json["location"],
#    "marital_Status": request.json["marital_Status"],
#    "gender": request.json["marital_Status"],
#    "population": request.json["population"],
#    }
#    values = (census["id"],census["census_Year"],census["location"],census["marital_Status"],census["marital_Status"],census["population"])
#    new_data = populationDAO.create(values)
#    census["id"] = new_data
#    return jsonify(values)

if __name__ == "__main__":
    app.run(debug=True)