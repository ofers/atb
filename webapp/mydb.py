import mysql.connector
from mysql.connector import errorcode, Error

config = {
    'user': 'root',
    'password': '1q2w3e',
    'host': '127.0.0.1',
    'raise_on_warnings': True,
    # 'OPTIONS': {
    #     'charset': 'utf8mb4',
    # }
}

DB_NAME = 'atb'

TABLES = {}
TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    "  `id` int(11) NOT NULL  AUTO_INCREMENT,"
    "  `emp_no` int(11) NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `department` varchar(16) NOT NULL,"
    "  PRIMARY KEY (`emp_no`),"
    "  KEY (id)"
    ") ENGINE=InnoDB")


def initdb():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    def create_database(cursor):
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8mb4'".format(DB_NAME))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            print("Database {} created successfully.".format(DB_NAME))
            cnx.database = DB_NAME
        else:
            print(err)
    #            exit(1)
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    cursor.close()
    cnx.close()


def add_emp(first_name, last_name, department, emp_no):
    cnx = mysql.connector.connect(**config, database=DB_NAME)
    cursor = cnx.cursor()
    emp_data = (first_name, last_name, department, emp_no)
    add_employee = ("INSERT INTO employees "
                    "(first_name, last_name, department, emp_no) "
                    "VALUES (%s, %s, %s, %s)")

    # Insert new employee
    try:
        cursor.execute(add_employee, emp_data)
    except mysql.connector.IntegrityError as err:
        print("Error: {}".format(err))
    else:
        print("Employee: {} was added.".format(emp_data))

    # Make sure data is committed to the database
    cnx.commit()
    cursor.close()
    cnx.close()


def get_emps_all():
    cnx = mysql.connector.connect(**config, database=DB_NAME)
    cursor = cnx.cursor(dictionary=True)
    query = ("SELECT id, first_name, last_name, department, emp_no FROM employees")
    cursor.execute(query)
    # for (first_name, last_name, department, emp_no) in cursor:
    #     print("First Name: {}, Last Name: {}, Department: {}, Emp ID: {}".format(
    #         last_name, first_name, department, emp_no))
    return cursor.fetchall()
    cnx.commit()
    cursor.close()
    cnx.close()


def del_emp(id):
    cnx = mysql.connector.connect(**config, database=DB_NAME)
    cursor = cnx.cursor()
    query = ("DELETE from employees where id={};".format(id))
    cursor.execute(query)
    cnx.commit()
    # cursor.execute("select * from employees where emp_no={};".format(emp_no))
    # records = cursor.fetchall().__str__()
    # if len(records) == 0:
    #     print("\nEmployee Deleted successfully ")
    # else:
    #     print(records)
    #     print("\nFaild to Delete Employee ")
    cursor.close()
    cnx.close()


def get_emp(emp_id):
    cnx = mysql.connector.connect(**config, database=DB_NAME)
    cursor = cnx.cursor(dictionary=True)
    query = ("select * from employees where id={}".format(emp_id))
    cursor.execute(query)
    return cursor.fetchall()
    cursor.close()
    cnx.close()


def update_emp(emp_id, first_name, last_name, department, emp_no):
    cnx = mysql.connector.connect(**config, database=DB_NAME)
    cursor = cnx.cursor(dictionary=True)

    query = ("UPDATE employees SET "
             "first_name = '" + first_name + "', "
             "last_name = '" + last_name + "', "
             "department = '" + department + "', "
             "emp_no = " + emp_no + " "
             "WHERE id = " + emp_id + " ")
    print(query)
#             "WHERE id={}".format(first_name, last_name, department, emp_no, emp_id))
    cursor.execute(query)
    cnx.commit()
    queryread = ("select * from employees where id={}".format(emp_id))
    cursor.execute(queryread)
    return cursor.fetchall()
    cursor.close()
    cnx.close()
