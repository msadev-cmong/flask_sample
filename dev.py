from flask import Flask, render_template, request
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

    return render_template('home.html', headquaters=labels, data=value)

@app.route('/sido/<sido>')
def show_detail(sido):

    if sido == '서울':
        sido = '소방'

    data = get_sub_data(sido)
    if data == None:
        list_data = [0, '경기']
    else:
        list_data = list(data)
        if list_data[1] == '소방':
            list_data[1] = '서울'

    return render_template('detail.html', data=list_data)

def get_main_data():
    conn = pymysql.connect(host='localhost', port=3306, user='test', password='test', db='test_db', charset='utf8')
    cursor = conn.cursor()
    sql_main =  'SELECT * FROM main'
    cursor.execute(sql_main)
    data = cursor

    conn.commit()
    conn.close()
    return data

def get_sub_data(sido_id):
    conn = pymysql.connect(host='localhost', port=3306, user='test', password='test', db='test_db', charset='utf8')
    cursor = conn.cursor()
    sql_main =  f'SELECT * FROM sub_table WHERE 시도 = "{sido_id}"'
    cursor.execute(sql_main)
    data = cursor

    conn.commit()
    conn.close()
    return data.fetchone()
    
if __name__ == "__main__":
     app.run(host="0.0.0.0", debug=True)