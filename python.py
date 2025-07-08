import MySQL.connector

custdb = mysql.connector.conntect(
	host="localhost",
	user="dbuser",
	password="dbpassword",
	database="ustomerdb"
)

custcursor = custdb.cursor()

custcursor.execute("SELECT * FROM customers")

custresult = custcurso.fetchall()

for x in custresult:
 print(x)