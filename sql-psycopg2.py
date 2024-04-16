import psycopg2

# connect to "chinook" database 
connection = psycopg2.connect(host="localhost", database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "artist"')


# Query 2 - select only the "Name" column from the "artist" table
# cursor.execute('SELECT "name" FROM "artist"')

# Query 3 - select only "Queen" from the "artist" table
# cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["Queen"])

# Query 4 - select only "artistid" #51 from the "artist" table
# cursor.execute('SELECT * FROM "artist" WHERE "artist_id" = %s', ["51"])

# Query 5 - select the albums with "artist_id" #51 from the "album" table
# cursor.execute('SELECT * FROM "album" WHERE "artist_id" = %s', ["51"])

# Query 6 - select the tracks where the composer is "Queen" from the "track" table
cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["Queen"])

# fetched the rusults (muliple)

results = cursor.fetchall()


# fetch the result (single)
# results = cursor.fetchone()

# close the conection
connection.close()

# print result
for result in results:
    print(result)