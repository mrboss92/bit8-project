from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'okhaldhunga',
  'salary': 'Rs.30000'
}, {
  'id': 2,
  'title': 'Frontend Developer',
  'location': 'kathmandu',
  'salary': 'Rs.35000'
}, {
  'id': 3,
  'title': 'Web Designer',
  'location': 'pokhara',
  'salary': 'RS.40000'
}, {
  'id': 4,
  'title': 'QA',
  'location': 'khotang',
  'salary': ''
}]

# creating html route
@app.route("/")
def project():
  return render_template('home.html', jobs=JOBS)

#creating api/json route
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
