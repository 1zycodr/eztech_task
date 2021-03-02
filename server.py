import pymysql
from app import app
from db_config import mysql
from flask import jsonify, Flask, request


@app.route('/area')
def area():
    try: 
        conn = mysql.connect()
        cursor = conn.cursor(
            pymysql.cursors.DictCursor
        )
        cursor.execute("SELECT * FROM area;")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    app.run(
        'localhost', 
        port=8080,
        debug=True
    )