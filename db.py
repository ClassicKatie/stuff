#!/usr/bin/env python

import MySQLdb

class Db(object):
    db_name = None
    connection = None
    cursor = None

    def __init__(self, db_name):
        creds = self.get_creds(db_name)
        self.db_name = db_name
        self.connection = MySQLdb.connect(
            db=creds['db_name'],
            host=creds['host'],
            user=creds['user'],
            passwd=creds['pw'],
        )
        self.cursor = self.connection.cursor()
        return

    # Takes db name. Returns a dict with relevant credentials
    def get_creds(self, db_name):
        pass

    def fetchone_hashref(self, query):
        self.cursor = self.connection.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def fetchrow_array(self, query):
        return

    def fetchall_tuple(self, query):
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def getvalue(self, query):
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return result

