import os
import ibm_db
from decouple import config

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

print(dsn)

try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database !! ")

except:
    print ("Unable to connect: ", ibm_db.conn_errormsg() )

