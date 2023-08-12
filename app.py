from flask import Flask 

app = Flask(__name__)

@app.route("/")
def project():
  return "project for 8 sem! we will be using python for this project"

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
