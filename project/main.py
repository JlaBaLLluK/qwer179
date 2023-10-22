from flask import Flask, render_template, request
import psycopg2
import os
from dotenv import load_dotenv

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
def hello_world():
    if request.method == 'GET':
        return render_template('add_data_page.html')

    return "response"


if __name__ == '__main__':
    app.run()
    cursor.close()
    connection.close()
