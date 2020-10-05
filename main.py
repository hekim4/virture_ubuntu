'''
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
'''

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>헬로</h1><br><a href="http://localhost:5000/test">이동하기</a>'

@app.route('/test')
def test():
    return render_template('post.html')

@app.route('/post', methods=['POST'])
def post():
    value = request.form['test']
    return value

#추가한 단락
@app.route('/reporters')
def reporters():
    import mariadb
    import sys
    try:
        conn = mariadb.connect(
            user="admink",
            password="p1234",
            host="localhost",
            port=3306,
            database="flask_db"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    cur = conn.cursor()
    cur.execute(
        'SELECT nickname, phone FROM reporter'
    )
    result = ""
    result += "<!DOCTYPE html>"
    result += "<html lang=\"kor\">"
    result += "<head>"
    result += " <meta charset=\"UTF-8\">"
    result += " <title>리포터</title>"
    result += "</head>"
    result += "<body>"
    result += "<ul>"

    for (nickname, phone) in cur:
        #print("{},{}".format(nickname, phone))
        result += "<li>{}, {}</li>".format(nickname, phone)
    result += "</ul>"
    result += "</body>"
    result += "</html>"
    '''
    <ul>
        <li>신사임당, 01011112222</li>
        <li>이순신, 01011112222</li>
        <!-- 생략 -->
        <li>홍길동, 01011112222</li>
    </ul>
    '''
    return result
#여기까지

if __name__ == '__main__':
    app.run()