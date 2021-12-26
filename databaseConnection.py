#Write a Python script for a database insertion using sqlalchemy
#Make a dummy XML, parse the XML(by using Python) and then insert into the database

#importing some attributes from sqlalchemy
from sqlalchemy import create_engine,Table, Column, Integer, String, MetaData, Date, Float,insert
#importing pymysql module for mysql connectivity for database
import pymysql
#importing xml module for parsing xml into sqlachemy for database insertion purpose
import xml.etree.ElementTree as ET

engine = create_engine("mysql+pymysql://saket:saket12345@127.0.0.1:3307/books_dtl", echo = True)
connection = engine.connect()
meta = MetaData()
#parsing the xml into tree variable
tree = ET.parse('XML_file.xml')
data = tree.findall('book')
# rows = len(data)
# column = len(data[0])+1
# print(data[0].tag)
# creating book_detail table
try:
    books_detail = Table(
        'books_detail',meta,
        Column('id',String(10)),
        Column('author_name',String(255)),
        Column('title', String(255)),
        Column('genre', String(100)),
        Column('price',Float,default=0.0),
        Column('publish_date',Date),
        Column('description',String(500))
    )
    meta.create_all(engine)
except:
    print('Some error occur in creation of table in database')
#inserting data into the database by iterating from xml file
for dta in data:
    try:
        id = dta.get('id')
        name = dta.find('author').text
        tit = dta.find('title').text
        gen = dta.find('genre').text
        pr = dta.find('price').text
        date = dta.find('publish_date').text
        describe = dta.find('description').text
        querry = insert(books_detail).values(id=id, author_name=name, title=tit, genre=gen, price=pr, publish_date=date, description=describe)
        connection.execute(querry)
        #print(id, name, tit, gen, pr, date, describe)
        print(id, ' inserted successfully ')
    except:
        print('Ooops some error occur in insertion')
print('All datas are saved in database succesfully')