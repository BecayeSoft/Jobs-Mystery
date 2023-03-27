import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class Scraper:

    def __init__(self, delay=3):
        self.delay=delay
        self.driver = webdriver.Chrome()

    def login(self, email, password):
        """Log in to linkedin.com"""

        self.driver.get('https://www.linkedin.com/login')
        time.sleep(self.delay)

        self.wait_till_element_ready(By.ID, "username")
        self.wait_till_element_ready(By.ID, "password")

        self.driver.find_element(By.ID, "username").send_keys(email)
        self.driver.find_element(By.ID, "password").send_keys(password, Keys.ENTER)


    def wait_till_element_ready(self, by, selector):
        """
        Wait for a given element to be ready

        :param by: the selector strategy. E.g.: By.ID, By.CLASS_NAME, etc.
        :param selector: the CSS selector according to the "By" strategy. E.g.: 'class name', 'id', etc.
        """

        colors = {'WARNING': '\033[93m', 'ERROR': '\033[91m'}
        try:
            WebDriverWait(self.driver, 8).until(EC.presence_of_element_located((by, selector)))
            time.sleep(self.delay)

        except TimeoutException:
            print(colors['WARNING'] + "Warning: Element has not been loaded!")
            pass


    def search_jobs(self, position, location):
        """
        Search jobs by entering position and location into the search bars.

        @:returns get_pagination_buttons(): the pagination buttons to navigate to the next page
        """

        self.driver.get("https://www.linkedin.com/jobs/")
        time.sleep(self.delay)

        # find the two search boxes: position and location
        self.wait_till_element_ready(By.CLASS_NAME, "jobs-search-box__text-input")
        search_bars = self.driver.find_elements(By.CLASS_NAME, "jobs-search-box__text-input")

        print("Found %d search bars" %len(search_bars))
        print(search_bars[3])

        # enter job position in the search  by keyword bar
        search_by_keyword_bar = search_bars[0]
        search_by_keyword_bar.send_keys(position)

        # enter job location in the search by location bar
        time.sleep(self.delay)
        search_by_location_bar = search_bars[3]
        search_by_location_bar.send_keys(location, Keys.RETURN)

        return self.get_pagination_buttons()


    def get_jobs_info(self):
        """
        Click on each job and extract its information:
        position, company, location, work mode (on site/remote), skills, description.
        """

        # Get the results of the first page
        self.wait_till_element_ready(By.CLASS_NAME, "jobs-search-results__list-item")
        time.sleep(self.delay)
        jobs_list = self.driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")

        jobs = []
        for job in jobs_list:

            # scroll the job div into view
            self.driver.execute_script("arguments[0].scrollIntoView();", job)
            time.sleep(self.delay)
            job.click()

            # get skills
            skills = self.get_job_skills()

            # description
            description = self.driver.find_elements(By.CLASS_NAME, "jobs-description-content__text")

            # position, company, location, and remote/on-site
            try:
                [position, company, location, work_mode] = job.text.split('\n')[:4]

                # store the information
                jobs.append([position, company, location, work_mode, skills, description])
                break
            except ValueError:
                position = job.text.split('\n')
                [company, location, work_mode] = ''
                print('job.text.split Error', job.text.split('\n'))
                # store the information
                jobs.append([position, company, location, work_mode, skills, description])

        return jobs


    def get_job_skills(self):
        """
        Click on the skills to displays them in a popup, then extract them
        """

        # click display skills popup
        self.wait_till_element_ready(By.CLASS_NAME, 'jobs-unified-top-card__job-insight-text-button')
        time.sleep(self.delay)
        view_skills_button = self.driver.find_element(By.CLASS_NAME, 'jobs-unified-top-card__job-insight-text-button')
        view_skills_button.click()

        # get skills list
        self.wait_till_element_ready(By.CLASS_NAME, "job-details-skill-match-status-list")
        time.sleep(self.delay)
        skills_list = self.driver.find_element(By.CLASS_NAME, 'job-details-skill-match-status-list')

        # get clean skills list
        skills_list_clean = skills_list.text.split('\n')
        skills_list_clean = list(filter(lambda skill: skill != 'Add', skills_list_clean))

        # close the skills list popup
        self.wait_till_element_ready(By.CLASS_NAME, 'artdeco-modal__dismiss')
        time.sleep(self.delay)
        close_popup_button = self.driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss')
        close_popup_button.click()

        return skills_list_clean


    def get_pagination_buttons(self):
        """Find the pagination buttons. These buttons are used to navigate through each page"""

        time.sleep(self.delay)
        # self.wait_till_element_ready(By.CLASS_NAME, "artdeco-pagination__pages")
        pagination = self.driver.find_element(By.CLASS_NAME, "artdeco-pagination__pages")
        pagination_buttons = pagination.find_elements(By.XPATH, './/button')

        print('pagination', pagination)

        return pagination_buttons


    def close_driver(self):
        self.driver.quit()

