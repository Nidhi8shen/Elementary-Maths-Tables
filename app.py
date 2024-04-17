from flask import Flask, render_template,request
#app
app = Flask(__name__)
#route
@app.route("/", methods=['GET'])
def table():
    if request.method == 'GET':
        number = 0
        multiply_with = 0
        to = 0
        if request.args.get('number') is not None and request.args.get('multiply_with') is not None and request.args.get('to') is not None:
            number = int(request.args.get('number'))
            to = int(request.args.get('to'))
            multiply_with = int(request.args.get('multiply_with'))
        return render_template('tables.html', number=number, multiply_with=multiply_with, to=to)