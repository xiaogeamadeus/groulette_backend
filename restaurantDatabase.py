# Author: Tianchen Wang
# Database of Restaurant.
# SQLite & Python 3.7

import sqlite3
restaurant = sqlite3.connect('Restaurant.db')
c = restaurant.cursor()
print("Database Open Successful")

cursor = c.execute("SELECT id, name, rating, address from RESTAURANT")
for row in cursor:
    print("ID = ", row[0])
    print("Name = ", row[1])
    print ("RATING = ", row[2])
    print ("ADDRESS = ", row[3], "\n")

print ("SELECT Successful")

# CREATE TABLE
# c.execute('''CREATE TABLE RESTAURANT
#          (ID INT PRIMARY KEY  NOT NULL,
#          NAME            CHAR(20) NOT NULL,
#          RATING          FLOAT  NOT NULL,
#          ADDRESS         CHAR(50),
#          LOCATION        CHAR(30));''')
# print ("Table Create Successful")


# INSERT VALUE INTO TABLE
# c.execute("INSERT INTO RESTAURANT (ID,NAME,RATING,ADDRESS,LOCATION) \
#           VALUES (1, 'KAFUGEN', 3.8, 'SAKYO-KU','12.33,131.1222')")

# Commit the changes(Only using in the INSERT or DELETE)
# restaurant.commit()

# 关闭数据库
restaurant.close()
