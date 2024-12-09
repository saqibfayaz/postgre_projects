import psycopg2 

#DB connection parameters
host = "pg.pg4r.com"
port = 5432
dbname = "pg4e_500bbbcc8c"
user = "pg4e_500bbbcc8c"
password = "your password"

try:
#connecting DB server
 conn = psycopg2.connect(
    host=host,
    port=port,
    dbname=dbname,
    user=user,
    password=password
 )
 cursor = conn.cursor()

 #drop and create table
 cursor.execute(" DROP TABLE IF EXISTS pythonseq;")
 cursor.execute("""
 CREATE TABLE pythonseq (
     iter INTEGER,
     val INTEGER           
 );
 """)

 # Inserting Pseudorandom numbers

 number = 148392
 for i in range(300):
    cursor.execute("INSERT INTO pythonseq (iter, val) VALUES (%s, %s);", (i +1, number))
    number = int((number * 22) / 7) % 1000000


 conn.commit()
 print("Successfully inserted 300 pseudorandom numbers into the pythonseq table.")

#error handle

except Exception as e:
    print(f"An error occured: {e}")
 
finally:
    if conn:
     cursor.close()
     conn.close()
