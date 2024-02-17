from distutils.log import debug 
from fileinput import filename 
from flask import *
app = Flask(__name__) 

@app.route('/') 
def main(): 
	return render_template("index.html") 

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
