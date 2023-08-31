# Jobs-Mystery

Scraping Data Science jobs from LinkedIn and Storing them into a SQL Server database.

See the notebook `Job-Mystery.ipynb`.

### Situation
As I was looking for an internship in Data Science, I needed to gain more information about the skills required to get a job in Data Science. However, manually gathering this info would have been a tedious task.
Inspired by some friends, I decided to create a bot to do it for me.

### Action
I use the following tools:
* Selenium: a perfect tool for interacting with a browser from the comfort of my PyCharm code.
* Python: elegant, beautiful, easy to use.

### Results
The bot was successfully launched and performed the following tasks:

* Scraped job postings from LinkedIn.
* Stored the scraped data into a Microsoft SQL Server database.

<img width="946" alt="image" src="https://user-images.githubusercontent.com/87549214/232181049-bd6870ee-613c-4985-b937-ac9a23ea7d73.png">

---

**TODO**
- [x] Build a scraper bot
- [x] Scrape jobs
- [ ] Create a word cloud of skills.

---


## Code Structure
The project is organized into the following files:

### `Scraper.py`
Scraper is the bot that interacts with LinkedIn to scrape jobs.

### `Database.py`
Database is an object that interacts with the database.

### `CSV.py`
CSV.py contains utility functions to save the data into a datframe.



## How to use it

1. Clone the repo
```
git clone https://github.com/BecayeSoft/Jobs-Mystery.git
cd Jobs-Mystery
```

2. Install the requirements

```bash
pip install -r requirements.txt
```

3. Set your credentials

The script below a your LinkedIn credentials to a file named "credentials.env".
Make sure to replace "youremail" and "yourpassword" with your LinkedIn credentials.

```bash
echo "EMAIL=youremail" > credentials.env
echo "PASSWORD=yourpassword" >> credentials.env
```

4. Run the main file

Edit the main file to change the job title and the location of the job.
Also, remove the database part if you don't have a Microsoft SQL Server database.

```python
python main.py
```
