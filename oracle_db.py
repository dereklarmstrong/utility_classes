#!/usr/bin/env python

import cx_Oracle

class OracleDB:
    """
    A class for connecting to an Oracle database and performing common database interactions such as querying, updating, inserting, and deleting data.
    """
    def __init__(self, username, password, host, port, service_name):
        """
        Initialize the connection to the Oracle database.

        Parameters:
        - username (str): The username to connect to the database with.
        - password (str): The password for the given username.
        - host (str): The hostname or IP address of the database server.
        - port (int): The port number to use for the connection.
        - service_name (str): The service name of the Oracle database.
        """
        self.conn = cx_Oracle.connect(username, password, f"{host}:{port}/{service_name}")
        self.cursor = self.conn.cursor()

    def query(self, query, bind_vars=None):
        """
        Execute a query on the database and return the results.

        Parameters:
        - query (str): The SQL query to execute.
        - bind_vars (tuple, optional): A tuple of bind variables to use in the query.

        Returns:
        - list: A list of tuples representing the rows returned from the query.
        """
        self.cursor.execute(query, bind_vars)
        return self.cursor.fetchall()

    def update(self, query, bind_vars=None):
        """
        Execute an update on the database.

        Parameters:
        - query (str): The SQL update query to execute.
        - bind_vars (tuple, optional): A tuple of bind variables to use in the query.

        Returns:
        - None
        """
        self.cursor.execute(query, bind_vars)
        self.conn.commit()

    def insert(self, query, bind_vars=None):
        """
        Execute an insert on the database.

        Parameters:
        - query (str): The SQL insert query to execute.
        - bind_vars (tuple, optional): A tuple of bind variables to use in the query.

        Returns:
        - None
        """
        self.cursor.execute(query, bind_vars)
        self.conn.commit()

    def delete(self, query, bind_vars=None):
        """
        Execute a delete on the database.

        Parameters:
        - query (str): The SQL delete query to execute.
        - bind_vars (tuple, optional): A tuple of bind variables to use in the query.

        Returns:
        - None
        """
        self.cursor.execute(query, bind_vars)
        self.conn.commit()
        
    def close(self):
        """
        Close the connection to the database.

        Returns:
        - None
        """
        self.cursor.close()
        self.conn.close()
