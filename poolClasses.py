import time
from time import time as my_timer

class Admin(object):
	def __init__(self):
		self

	# def viewTables(self):

class PoolTable(object):

	def __init__(self,noOfTables):
		self.noOfTables = noOfTables
		self.status = "Available"

	def yes_occupied(self):
		self.status = "Closed"
		self.start = my_timer()

	def checkOut(self):
		self.status = "Available"
		self.end = my_timer()
		self.totalTime = self.end - self.start


table1 = PoolTable(1)
# ____________________________________
table2 = PoolTable(2)
# ____________________________________
table3 = PoolTable(3)
# ____________________________________
table4 = PoolTable(4)
# ____________________________________
table5 = PoolTable(5)
# ____________________________________
table6 = PoolTable(6)
# ____________________________________
table7 = PoolTable(7)
# ____________________________________
table8 = PoolTable(8)
# ____________________________________
table9 = PoolTable(9)
# ____________________________________
table10 = PoolTable(10)
# ____________________________________
table11 = PoolTable(11)
# ____________________________________
table12 = PoolTable(12)
# ____________________________________
