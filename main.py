import Scraper
import Database
import os

scraper = Scraper()

# Login
email = os.getenv('Email')
password = os.getenv('Password')
print('email', email)

scraper.login(email, password)

# Search
scraper.search_jobs(title="data science", location="canada")

# Get Jobs Information
jobs = scraper.get_jobs_info()

# Save to Database
db = Database()
conn = db.connect()

db.save_jobs(conn, jobs)

db.close_connection(conn)