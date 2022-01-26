import xml.etree.ElementTree as ET
import sqlite3
from django.db.models.fields import NullBooleanField

tree = ET.parse('categories.xml')
category = tree.findall('Category')
conn = sqlite3.connect('C:/Users/RaymaN/Documents/Desafios_Tecnicos_Entrevistas/Aflore/db.sqlite3')


for item in category:
    try:
        BestOfferEnabled=item.find('BestOfferEnabled').text
        AutoPayEnabled=item.find('AutoPayEnabled').text
        
    except:
        BestOfferEnabled=''
        AutoPayEnabled=''
    try:
        LeafCategory=item.find('LeafCategory').text    
    except:
        LeafCategory=''

    CategoryID=item.find('CategoryID').text
    CategoryLevel=item.find('CategoryLevel').text
    CategoryName=item.find('CategoryName').text
    CategoryParentID=item.find('CategoryParentID').text
    
    cat='''INSERT INTO Categorias_Ebay_category('BestOfferEnabled',
                   'AutoPayEnabled',
                    'CategoryID',
                    'CategoryLevel',
                    'CategoryName',
                    'CategoryParentID_id',
                    'LeafCategory') VALUES(?,?,?,?,?,?,?)'''
    c = conn.cursor()
    c.execute(cat,(BestOfferEnabled,AutoPayEnabled,CategoryID,CategoryLevel,CategoryName,CategoryParentID,LeafCategory))
    conn.commit()   
    print("Data inserted successfully.")           
    