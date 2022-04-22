from flask import Flask, render_template
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    data = get_main_data()

    labels = []
    value = []
    for item in data:
        labels.append(item[1])
        value.append(item[2])

    return render_template('test.html', headquaters=labels, data=value)

def get_main_data():
    conn = pymysql.connect(host='mysql.sil', port=3306, user='test', password='Test!234', db='test_db', charset='utf8')
    cursor = conn.cursor()
    sql_main =  'SELECT * FROM main'
    cursor.execute(sql_main)
    data = cursor

    conn.commit()
    conn.close()
    return data
    
if __name__ == "__main__":
     app.run(host="0.0.0.0")