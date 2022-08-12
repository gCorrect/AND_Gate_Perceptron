import mysql.connector
# 2D---------------------------------
def loadPlotData(tablename):
    # database connection
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perceptron"
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
    # print("Result for c1: \n",result_c1)
    # cursor, execution, result -> C2
    c2 = mydb.cursor()
    query = "SELECT * FROM "+tablename+" WHERE EO=1"
    c2.execute(query)
    result_c2 = c2.fetchall()
    # print("Result for c2: \n",result_c2)
    # # x1[],y1[]        
    for row in result_c1:
        x1.append(row[0])
        y1.append(row[1])
    # x2[],y2[]        
    for row in result_c2:
        x2.append(row[0])
        y2.append(row[1])
    return x1,y1,x2,y2
def loaddata(tablename):
    # database connection
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perceptron"
    )
    # cursor, execution, result -> C1
    cursor = mydb.cursor()
    query = "SELECT * FROM "+tablename
    cursor.execute(query)
    result = cursor.fetchall()
    print("---------------------------")
    print("Database Result for all: \n")
    print(result)
    return result
def loadTupleData(tablename):
    # database connection
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perceptron"
    )
    # cursor, execution, result -> C1
    cursor = mydb.cursor()
    query = "SELECT x1,x2 FROM "+tablename
    cursor.execute(query)
    result = cursor.fetchall()
    query = "SELECT EO FROM "+tablename
    cursor.execute(query)
    resultEO = cursor.fetchall()
    print("---------------------------")

    print("Result for EO: \n")
    print(resultEO)
    print(type(resultEO))

    alldata= list(zip(result,resultEO))
    return alldata
def loaddataPerCategory(tablename):
    # database connection
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perceptron"
    )
    # cursor, execution, result -> C1
    cursor = mydb.cursor()
    query = "SELECT x1,x2 FROM "+tablename+ " WHERE category='C1'"
    cursor.execute(query)
    result = cursor.fetchall()
    print("---------------------------")
    print("Result for C1: \n")
    print(result)
    print(type(result))
    return result
# 3D---------------------------------
def load3DPlotData(tablename):
    # database connection
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perceptron"
    )
    # variables of data
    x1 = []
    y1 = []
    z1 = []
    x2 = []
    y2 = []
    z2 = []
    # cursor, execution, result -> C1
    c1 = mydb.cursor()
    query = "SELECT x1,x2,x3 FROM "+tablename+" WHERE EO=0"
    c1.execute(query)
    result_c1 = c1.fetchall()
    # print("Result for c1: \n",result_c1)
    # cursor, execution, result -> C2
    c2 = mydb.cursor()
    query = "SELECT x1,x2,x3 FROM "+tablename+" WHERE EO=1"
    c2.execute(query)
    result_c2 = c2.fetchall()
    # print("Result for c2: \n",result_c2)
    # # x1[],y1[]        
    for row in result_c1:
        x1.append(row[0])
        y1.append(row[1])
        z1.append(row[2])
    # x2[],y2[]        
    for row in result_c2:
        x2.append(row[0])
        y2.append(row[1])
        z2.append(row[2])
    return x1,y1,z1,x2,y2,z2
def load3DTupleData(tablename):
    # database connection
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perceptron"
    )
    # cursor, execution, result -> C1
    cursor = mydb.cursor()
    query = "SELECT x1,x2,x3 FROM "+tablename
    cursor.execute(query)
    result = cursor.fetchall()
    query = "SELECT EO FROM "+tablename
    cursor.execute(query)
    resultEO = cursor.fetchall()
    # print("---------------------------\n","Result for EO: \n", resultEO,"\n type: ", type(resultEO))    
    alldata= list(zip(result,resultEO))
    return alldata
