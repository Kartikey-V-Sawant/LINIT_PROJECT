from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
import mysql.connector
import pandas as pd
conn=mysql.connector.connect(user='root',password='',host='localhost',database='test')
Select_stmt=("Select * from mstcountry")
cursor=conn.cursor()
cursor.execute(Select_stmt)


Countries=cursor.fetchall()
def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render)
     
