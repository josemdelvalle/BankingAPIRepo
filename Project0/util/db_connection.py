import psycopg2
from psycopg2._psycopg import OperationalError


def create_connection():
    try:
        conn = psycopg2.connect(
            database='',
            user='',
            password='',
            host='',
            port='',
        )

        return conn
    except OperationalError as e:
        print(f"{e}")
        return conn


connection = create_connection()

# import psycopg2
# from psycopg2 import Error
#
# try:
#     # Connect to an existing database
#     connection = psycopg2.connect(
#         database='postgres',
#         user='JoseMDelValle',
#         password='esoj9505',
#         host='josepostgress.cumlvsjhtfvq.us-east-2.rds.amazonaws.com',
#         port='5432')
#
#     # Create a cursor to perform database operations
#     cursor = connection.cursor()
#     # Print PostgreSQL details
#     print("PostgreSQL server information")
#     print(connection.get_dsn_parameters(), "\n")
#     # Executing a SQL query
#     cursor.execute("SELECT version();")
#     # Fetch result
#     record = cursor.fetchone()
#     print("You are connected to - ", record, "\n")
#
# except (Exception, Error) as error:
#     print("Error while connecting to PostgreSQL", error)
# finally:
#     if (connection):
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")
