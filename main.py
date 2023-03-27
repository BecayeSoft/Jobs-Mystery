from Scraper import Scraper
import Database
import CSV
import os
from dotenv import load_dotenv


scraper = Scraper()

# load the credentials
load_dotenv('credentials.env')

# Login
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')
print('email', email)
scraper.login(email, password)

# Search jobs by title and location and get pagination buttons
pagination_buttons = scraper.search_jobs(position="data science", location="canada")

# Loop through each page
all_jobs = []
for button in pagination_buttons:
    # get the jobs of the current page
    current_page_jobs = scraper.get_jobs_info()
    all_jobs.append(current_page_jobs)

    # navigate to the next page
    button.click()

# Save to Database
db = Database()
conn = db.connect()
db.save_jobs(conn, all_jobs)
db.close_connection(conn)

# Save to CSV file
CSV.save_to_csv(all_jobs,
                colnames=['position', 'company', 'location', 'work_mode', 'skills', 'description'],
                filename='jobs.csv')


# close the browser
scraper.close_driver()