# Jobs-Mystery

Scraping Data Science jobs from LinkedIn and Storing them into a SQL Server database.

### Situation
As I was looking for an internship in a Data Science, I needed to gain more information about the skills needed to get a job in Data Science. But this can be a tedious task.
I got inspired by some friends and I thought I should create a bot to do that for me. 

### Action
What tool could as act a human?
* Selenium: a perfect tool for interacting with a browser from the confort of my PyCharm code.
* Python: an elegant, beautiful language.

### Results
I launched the bot out there: 
* The bot went on to scrape some jobs.
* The results were stored into a Microsoft SQL server database.

<img width="946" alt="image" src="https://user-images.githubusercontent.com/87549214/232181049-bd6870ee-613c-4985-b937-ac9a23ea7d73.png">

When the bot will scrape enough jobs, I might be interesting to visualize the skills required with a word of skills.

---

**TODO**
- [x] Build a scraper bot
- [x] Scrape jobs
- [ ] Create a word cloud of skills.

---

## Code Structure

### `Scraper.py`
Scraper is the bot that interacts with LinkedIn to scrape jobs.

### `Database.py`
Database is an object that interacts with the database.

### `CSV.py`
CSV.py contains utility functions to save the data into a datframe.
