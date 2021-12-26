from sqlalchemy import create_engine,MetaData
import pymysql
engine = create_engine("mysql+pymysql://<root>:<''>@<localhost>/book",echo = True)
meta = MetaData()
