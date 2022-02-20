from flask import Flask, request, jsonify
from replit import db
app = Flask(__name__)


blocked = True


@app.route("/")
def index():
  return jsonify(
    hello = "world"
  )

@app.route("/info")
def info():
  return jsonify(
    error = False,
    blocked = blocked
  )

@app.route("/url", methods = ['POST','GET'])
def url():
  if request.method == 'POST':
    id = request.form["id"]
    if id in db:
      return jsonify(
        error = False,
        url = db[id]
      )
    else:
      return jsonify(
        error = True,
        code = 3
      )
  else:
    return jsonify(
      error = True,
      code = 1
    )

@app.route("/new", methods = ['POST','GET'])
def new():
  if request.method == 'POST':
    if blocked == False:
      if request.form["url"] is not None:
        f = open('lastnum.txt', 'r+')
        last = int(f.read())
        url = str(last + 1)
        db[url] = request.form["url"]
        f.close()
        f = open('lastnum.txt', 'w+')
        f.write(url)
        f.close()
        return jsonify(
          error = False,
          id = url
        )
      else:
        return jsonify(
          error = True,
          code = 2
        )
    else:
      return jsonify(
        error = True,
        code = 4
      )
  else:
    return jsonify(
      error = True,
      code = 1
    )

@app.route("/report", methods = ['POST','GET'])
def report():
  if request.method == 'POST':
    if request.form["report"] is not None:
      rf = open('reports.txt', 'r+')
      rl = rf.read()
      rl = rl + "\n" + str(request.form["report"])
      rf.close()
      rf = open('reports.txt', 'w+')
      rf.write(rl)
      rf.close()
      return jsonify(
        error = False,
        id = url
      )
    else:
      return jsonify(
        error = True,
        code = 2
      )
  else:
    return jsonify(
      error = True,
      code = 1
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=False)
