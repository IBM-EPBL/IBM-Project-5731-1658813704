from flask import Flask
import ibm_db
from decouple import config

# Database Connectivity

dsn_hostname = config('HOSTNAME')
dsn_uid = config('UID')        
dsn_pwd = config('PASSWORD')  

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = config('DATABASE')            
dsn_port = config('PORT')                
dsn_protocol = "TCPIP"        
dsn_security = "SSL"             

dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security)

try:
    conn = ibm_db.connect(dsn, "", "")

except:
    print ("Unable to connect: ", ibm_db.conn_errormsg() )

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = config('FLASK_KEY')
   

    from .views import news
    from .auth import auth
    from .categories import category

    app.register_blueprint(news,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    app.register_blueprint(category,url_prefix='/')


    return app

