from flask import Flask, render_template, jsonify

app = Flask(__name__)

CAFES = [
  {
    'id':1,
    'name': 'Costa',
    'location': 'Headingley'
  },
  {
    'id':2,
    'name': 'Starbucks',
    'location': 'Moortown'
  },
{
    'id':3,
    'name': 'Nero',
    'location': 'Alwoodley'
  },
  
]


@app.route("/")
def hello_world():
  return render_template("index.html", cafes=CAFES)

@app.route("/api/cafes")
def list_cafes():
  return jsonify(CAFES)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
