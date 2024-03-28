import sqlite3

# 1. Połączenie z bazą danych (lub jej stworzenie, jeśli nie istnieje)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

