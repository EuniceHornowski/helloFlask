from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
	return render_template('index.html')
	
@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
	return render_template('form.html')

@app.route('/gateaux')
def gateaux():
	return render_template('gateaux.html')

app.run(debug=True)
