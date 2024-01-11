import os
import pandas as pd
import mysql.connector
import flask 

mydb = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "mysql4703",
    database= "phd_papers"
)

