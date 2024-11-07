import mysql.connector

cnx = mysql.connector (user = 'root', password = 'password',
                       host = '127.0.0.1',
                       database = 'employees')

                       
cnx.close()