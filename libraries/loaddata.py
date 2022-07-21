import matplotlib.pyplot as plt
import numpy as np
import mysql.connector
def loadPlotdata(tablename):
    # database connection
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mlCook1",
    database="test"
    )
    # variables of data
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    # cursor, execution, result -> C1
    c1 = mydb.cursor()
    query = "SELECT * FROM "+tablename+" WHERE EO=0"
    c1.execute(query)
    result_c1 = c1.fetchall()
    # print
    print("Result for c1: ")
    print(result_c1)
    # cursor, execution, result -> C2
    c2 = mydb.cursor()
    query = "SELECT * FROM "+tablename+" WHERE EO=1"
    c2.execute(query)
    print("Result for c2: ")
    result_c2 = c2.fetchall()
    # print
    print(result_c2)
    # x1[],y1[]        
    for row in result_c1:
        x1.append(row[1])
        y1.append(row[2])
    # x2[],y2[]        
    for row in result_c2:
        x2.append(row[1])
        y2.append(row[2])
    return x1,y1,x2,y2
def loaddata(tablename):
    # database connection
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mlCook1",
    database="test"
    )
    # cursor, execution, result -> C1
    cursor = mydb.cursor()
    query = "SELECT * FROM "+tablename
    cursor.execute(query)
    result = cursor.fetchall()
    # print
    print("Result for all Data: \n")
    print(result)
    print("---------------------------")
    return result
    