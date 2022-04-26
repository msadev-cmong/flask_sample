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

@app.route('/<sido>/')
def sub_graph(sido):

    if sido == "서울":
        sido = "소방"

    data = get_sub_data(sido)

    labels = ["오토바이", "운전자", "기타 탈것", "자전거", "보행자", "동승자"]
    val = []
    for i in data:
        val.append(i[2:]) 

    return render_template('sub.html',headquaters=labels, data=val[0])

def get_main_data():
    conn = pymysql.connect(host='mysql-svc', port=3306, user='test', password='test', db='test_db', charset='utf8')
    cursor = conn.cursor()
    sql_main =  'SELECT * FROM main'
    cursor.execute(sql_main)
    data = cursor

    conn.commit()
    conn.close()
    return data

def get_sub_data(sido_data):
    conn = pymysql.connect(host='mysql-svc', port=3306, user='test', password='test', db='test_db', charset='utf8')
    cursor = conn.cursor()
    sql_main =  f'SELECT * FROM sub_table where 시도 = "{sido_data}"'
    cursor.execute(sql_main)
    data = cursor

    conn.commit()
    conn.close()
    return data
    
if __name__ == "__main__":
     app.run(host="0.0.0.0")