from flask import Flask, render_template
app = Flask(__name__)

listi=[
	["Guðjón Atli Vignisson","2210022020"],
	["Guðmundur Árni Vilhelmsson","2908021013"],
	["Vanessa Vaughn","3105022215"],
	["Jóakim Aðalönd","5555555555"]
]

@app.route('/')
def index():
	return render_template("index.tpl")

@app.route('/kt')
def kt():
	return render_template("kennitala.tpl", listi=listi)

@app.route('/kt/<kt1>')
def summa(kt1):
	i=0
	for x in kt1:
		i=i+int(x)
	return render_template("ktGot.tpl", i=i, kt1=kt1)

@app.errorhandler(404)
def error404(error):
	return "Síðan var ekki fundin", 404

if __name__ == "__main__":
	app.run(debug=True)