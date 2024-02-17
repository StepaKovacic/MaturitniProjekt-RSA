from distutils.log import debug 
from fileinput import filename 
from flask import *
app = Flask(__name__) 

# @app.route('/ne') 
# def main(): 
# 	return render_template("index.html") 

@app.route("/desifrovani")
def desifrovani():
	return render_template("desifrovani.html")

@app.route("/zasifrovani")
def zasifrovani():
	return render_template("sifrovani.html")

@app.route("/generovani_klicu")
def keygen():
	return render_template("keygen.html")

@app.route("/programatorska_dokumentace")
def programatorska_dokumentace():
	return render_template("programatorska_dokumentace.html")

@app.route("/")
def index():
	return render_template("uzivatelska_dokumentace.html")

@app.route('/uspech', methods = ['POST']) 
def success(): 
	if request.method == 'POST': 
		f = request.files['file'] 
		f.save("demo.txt") 
		d = open("demo.txt", "r")
		
		x = d.read()
		return render_template("uspech.html", name = f.filename, text = x) 

if __name__ == '__main__': 
	app.run(debug=True)
