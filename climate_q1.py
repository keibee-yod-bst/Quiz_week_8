import matplotlib.pyplot as plt
import sqlite3
connection = sqlite3.connect(r'climate.db')
cursor = connection.cursor()


cursor.execute("SELECT * FROM Year")
print("fetchall:")
result = cursor.fetchall() # Return all (remaining) rows of a query result as a list.
for r in result:
    print(r)
cursor.execute("SELECT * FROM Year")
print("\nfetch one:")
res = cursor.fetchone() # Return the next row query result set as a tuple.
Return None if # no more data is available.
print(res)
connection.close()


years = []
co2 = []
temp = []

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 
