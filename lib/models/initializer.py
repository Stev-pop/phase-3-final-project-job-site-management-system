# models/initializer.py
import sqlite3

CONN = sqlite3.connect('job_site.db')
CURSOR = CONN.cursor()