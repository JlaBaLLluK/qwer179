from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/add-data/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return render_template('add_data_page.html')

    data_from_form = request.form['name']
    print(request.form.keys())
    return data_from_form


if __name__ == '__main__':
    app.run()
