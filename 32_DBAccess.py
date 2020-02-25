import sqlite3
from employee import Employee

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('./Data/employee.db')

cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS employees (
                first text,
                last text,
                pay integer
                )""")

cur.execute("INSERT INTO employees values('Ramesh', 'Theivendran',10000000)")
cur.execute("INSERT INTO employees values('Aruna', 'Ramesh',75000)")
cur.execute("INSERT INTO employees values('Vineha', 'Ramesh',200000)")
cur.execute("INSERT INTO employees values('Vinusha', 'Ramesh', 200000)")
conn.commit()

emp1 = Employee('Bob','Smith',100000)
emp2 = Employee('Joe', 'Smith',230000)
emp3 = Employee('Bill', 'Smith', 250000)
emp4 = Employee('Will', 'Smith', 250000)

cur.execute("INSERT INTO employees values(?, ?, ?)", (emp1.first, emp1.last, emp1.pay))
cur.execute("INSERT INTO employees values(?, ?, ?)", (emp2.first, emp2.last, emp2.pay))
cur.execute("INSERT INTO employees values(?, ?, ?)", (emp3.first, emp3.last, emp3.pay))
cur.execute("INSERT INTO employees values(:first, :last, :pay)", {'first':emp3.first,'last':emp3.last, 'pay':emp3.pay})
conn.commit()

cur.execute("SELECT * FROM employees")
data = cur.fetchall()

print("No of rows in the table: {}".format(len(data)))
for row in data:
    print(row)

conn.close()
