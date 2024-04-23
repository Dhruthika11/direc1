from flask import Flask, render_template, request
import mysql.connector
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Dhruthika'
app.config['MYSQL_DB'] = 'imdb'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    a_1_data = []
    a_2_data = []
    a_3_data = []
    a_4_data = []
    a_5_data = []


    if request.method == 'POST':
        bond = request.form['expiry_date']
        name_of_the_party = request.form['expiry_date']
        expiry_date = request.form['expiry_date']
        purchase_date = request.form['purchase_date']
        purchaser_name = request.form['purchaser_name']
        # AI: Use a different name for the query parameters
        # Example: cur.execute("select `name` from `names` where `name` like %s limit 5;", ('%' + box + '%',))

        # AI: Query the 'output_table1' and 'output_table2' tables
        cursor = mysql.connection.cursor()
        cursor.execute("select * from output_table2 where Bond Number like %s", ('%' + bond + '%',))
        a_1_data = cursor.fetchall()
        cursor.close()

        cursor = mysql.connection.cursor()
        cursor.execute("select * from output_table2 where Name of the Party = like %s;", ('%' + name_of_the_party + '%',))
        a_2_data = cursor.fetchall()
        cursor.close()

        cursor = mysql.connection.cursor()
        cursor.execute("select * from output_table1 where Date of Expiry = like %s;", ('%' + expiry_date + '%',))
        a_3_data = cursor.fetchall()
        cursor.close()

        cursor = mysql.connection.cursor()
        cursor.execute("select * from output_table1 where Date of Purchase = like %s ;", ('%' + purchase_date + '%',))
        a_4_data = cursor.fetchall()
        cursor.close()

        cursor = mysql.connection.cursor()
        cursor.execute("select * from output_table1 where Name of the Purchaser = like %s;", ('%' + purchaser_name + '%',))
        a_5_data = cursor.fetchall()
        cursor.close()

    return render_template('index.html', a_1_data=a_1_data, a_2_data=a_2_data, a_3_data=a_3_data, a_4_data=a_4_data, a_5_data=a_5_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="80", debug=True)