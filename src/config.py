# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)
import os

rds_host, rds_port  = os.environ['rds_endpoint'].split(":")
rds_uname = os.environ['rds_username']
rds_passwd= os.environ['rds_password']
rds_db_name = os.environ['rds_dbname']

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'+rds_uname+':'+rds_passwd+'@'+rds_host+':'+rds_port+'/'+rds_db_name

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'
