from app import app
from flaskext.mysql import MySQL
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'shopuser'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Fks#23pq17$Dbvr'
app.config['MYSQL_DATABASE_DB'] = 'areas'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)