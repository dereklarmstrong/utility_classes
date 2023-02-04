import cx_Oracle

class OracleDB:
    """
    OracleDB class provides a convenient interface for connecting and interacting with an Oracle database.

    Attributes:
        connection: A cx_Oracle connection object.
        cursor: A cx_Oracle cursor object.
    """

    def __init__(self, username, password, host, port, sid):
        """
        The constructor takes the credentials required to connect to the Oracle database.

        Args:
            username: The username to connect to the database.
            password: The password to connect to the database.
            host: The host name or IP address of the database server.
            port: The port number of the database server.
            sid: The sid (system identifier) of the database.
        """
        try:
            self.connection = cx_Oracle.connect(
                username, password, f"{host}:{port}/{sid}")
            self.cursor = self.connection.cursor()
            print("Connected to the database.")
        except cx_Oracle.DatabaseError as e:
            print("Error while connecting to the database:", e)

    def query(self, sql, parameters=None):
        """
        The method executes a SELECT statement on the database.

        Args:
            sql: The SELECT statement.
            parameters: A tuple of bind variables. (default is None)

        Returns:
            A list of tuples representing the rows returned by the SELECT statement.
        """
        try:
            self.cursor.execute(sql, parameters)
            return self.cursor.fetchall()
        except cx_Oracle.DatabaseError as e:
            print("Error while executing the SELECT statement:", e)

    def execute_(self, sql, parameters=None):
        """
        The method executes an INSERT, UPDATE, or DELETE statement on the database.

        Args:
            sql: The INSERT, UPDATE, or DELETE statement.
            parameters: A tuple of bind variables. (default is None)

        Returns:
            The number of rows affected by the statement.
        """
        try:
            self.cursor.execute(sql, parameters)
            rows_affected = self.cursor.rowcount
            self.connection.commit()
            return rows_affected
        except cx_Oracle.DatabaseError as e:
            print("Error while executing the INSERT, UPDATE, or DELETE statement:", e)
            self.connection.rollback()

    def close(self):
        """
        The method closes the connection to the database.

        Returns:
            None
        """
        try:
            self.cursor.close()
            self.connection.close()
            print("Connection to the database closed.")
        except cx_Oracle.DatabaseError as e:
            print("Error while closing the connection:", e)
