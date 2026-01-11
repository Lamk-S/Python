import sqlite3

def conectar():
    return sqlite3.connect("Intermediate/07-Exceptions-ErrorHandling/DB_SQLite/db_employees.db")