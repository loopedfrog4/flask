from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def Hello():
   if request.method == 'POST':
      taskContent = request.form['search'];
      return taskContent
   else:
      return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)