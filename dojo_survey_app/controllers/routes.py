from flask import app
from dojo_survey_app import app
from flask import render_template, redirect, request, session, flash
from dojo_survey_app.models.dojos import Dojo

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = {
        'name': request.form['name'],
        'location': request.form['location'],
        'language': request.form['language'],
        'comment': request.form['comment']
    }
    if not Dojo.validate_survey(request.form):
        return redirect("/")
    Dojo.save(request.form)
    name = Dojo.get_id_by_name(data)
    dojo_id = name[0]['id']
    return redirect(f'/result/{dojo_id}')

@app.route('/result/<int:dojo_id>')
def result(dojo_id):
    data = {
        "id": dojo_id,
    }
    dojo = Dojo.get_info_by_id(data)
    print("print:", dojo)
    return render_template('result.html', dojo = dojo, dojo_id = dojo_id)

if __name__ == "__main__":
    app.run(debug=True)