from flask import Flask, url_for, render_template, request, redirect
from Calculations.MolarMass import calculateMolarMass
from Calculations.Mols import calculateMols
from Calculations.Mass import calculateMass

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('Molarmass'):
            result = request.form
            formula = result['Formula']
            mm = calculateMolarMass(formula)
            return render_template("index.html", mm=mm, formula=formula)
        
        elif request.form.get("mass"):
            result = request.form
            formula = result['FormulaM']
            mols = result['molsmass']
            mass = calculateMass(formula, mols)
            return render_template("index.html", mass=mass, formula=formula)
        
        elif request.form.get("mols"):
            result = request.form
            formula = result['FormulaM']
            mass = result['molsmass']
            mols = calculateMols(formula, mass)
            return render_template("index.html", mols=mols, formula=formula)
    return render_template("index.html", mm=None, formula=None)


if __name__ == "__main__":
    app.run(debug=True)