import psycopg2

class PostgreSQLDB:
    """
    Class to interface with a PostgreSQL database. 
    Supports query, insert, update, and delete operations.
    """

    def __init__(self, host, database, user, password):
        """
        Connect to the database during object creation.
        :param host: host name or IP address
        :param database: name of the database
        :param user: database user name
        :param password: database user password
        """
        self.conn = None
        self.cursor = None
        try:
            self.conn = psycopg2.connect(
                host=host,
                database=database,
                user=user,
                password=password
            )
            self.cursor = self.conn.cursor()
            print("Connected to PostgreSQL database")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL database", error)

    def query(self, sql):
        """
        Execute a SELECT statement.
        :param sql: SELECT statement
        :return: list of tuples with query result
        """
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except (Exception, psycopg2.Error) as error:
            print("Error while executing SELECT statement", error)

    def insert(self, sql, values):
        """
        Execute an INSERT statement.
        :param sql: INSERT statement
        :param values: values to insert
        :return: None
        """
        try:
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Data inserted successfully")
        except (Exception, psycopg2.Error) as error:
            print("Error while executing INSERT statement", error)

    def update(self, sql, values):
        """
        Execute an UPDATE statement.
        :param sql: UPDATE statement
        :param values: values to update
        :return: None
        """
        try:
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Data updated successfully")
        except (Exception, psycopg2.Error) as error:
            print("Error while executing UPDATE statement", error)

    def delete(self, sql, values=None):
        """
        Execute a DELETE statement.
        :param sql: DELETE statement
        :param values: values to delete
        :return: None
        """
        try:
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Data deleted successfully")
        except (Exception, psycopg2.Error) as error:
            print("Error while executing DELETE statement", error)

    def close(self):
        """
        Close the cursor and database connection.
        :return: None
        """
        if self.cursor:
            self.cursor.close()
