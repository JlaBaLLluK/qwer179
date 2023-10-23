from flask import Flask, render_template, request
import psycopg2
import os
from dotenv import load_dotenv
import json

app = Flask(__name__)
load_dotenv()
connection = psycopg2.connect(
    host="localhost",
    database="task_db",
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"]
)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS data_table("
               "id serial primary key,"
               "data jsonb);")
connection.commit()


@app.route('/add-data/', methods=['POST', 'GET'])
def add_data():
    if request.method == 'POST':
        data = json.dumps(request.form)
        cursor.execute("INSERT INTO data_table (data) VALUES (%s})", (data,))
        connection.commit()

    return render_template('add_data_page.html')


@app.route('/get-data/')
def get_data():
    cursor.execute("SELECT * FROM data_table;")
    data_from_table = cursor.fetchall()
    data = {}
    for row in data_from_table:
        data[str(row[0])] = row[1]

    return render_template("all_data_page.html", data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    cursor.close()
    connection.close()
