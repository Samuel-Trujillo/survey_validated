from flask import render_template,redirect,request,session,redirect, flash
from flask.helpers import url_for
from flask_app import app
from ..model.dojo import Dojo
@app.route('/')
def index():
    
    return render_template("index.html")

@app.route('/results/<int:dojo>')
def show(dojo):
    data = {
        'id': dojo
    }

    return render_template("show.html", dojo = Dojo.show_input(data) )


@app.route('/result_math', methods= ['POST'])
def sumbit_result():
    if not Dojo.validate_data(request.form):
        return redirect('/')
        
    dojo = Dojo.create(request.form)

    

    return redirect(f'/results/{dojo}')





if __name__ == "__main__":
    app.run(debug=True)
