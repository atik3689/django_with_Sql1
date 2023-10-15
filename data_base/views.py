from django.shortcuts import render
from django.http import HttpResponse
from blog.models import  login_data
import mysql.connector

def aboutUs(request):
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="login"
    )
    mycursor = mydb.cursor()


    if request.method=="POST":
        username=(request.POST['num1'])
        password=(request.POST['password'])
        
        

        a=username

        b=password


         
        sql="insert into login_data(email,password) values('"+a+"','"+b+"')"
        mycursor.execute(sql)

        mydb.commit()

        print(mycursor.rowcount,"record inserted.")



    return render (request,"index.html")