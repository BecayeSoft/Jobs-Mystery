import pypyodbc as odbc


class Database:
    def __init__(self, driver='SQL Server', server='.', database='LinkedIn'):
        self.driver_name = driver
        self.server_name = server
        self.database_name = database

    
    def connect(self):
        connection_string = f"""
            DRIVER={{{self.driver_name}}};
            SERVER={{{self.server_name}}};
            DATABASE={{{self.database_name}}};
            Trust_Connection=yes;
        """
        
        conn = odbc.connect(connectString=connection_string)
        return conn
    

    def close_connection(conn):
        conn.close()


    def save_jobs(conn, jobs):
        """
        Inserts the jobs into the databse

        :param jobs: jobs to be inserted
        :return:
        """

        cursor = conn.cursor()
        insert_query = "INSERT INTO Jobs (position, company, location, work_mode, skills, details) VALUES (?, ?, ?, ?, ?, ?)"

        for job in jobs:
            position = job[0]
            company = job[1]
            location = job[2]
            work_mode = job[3]
            skills = job[4]
            details = job[5]

            # transofrm skills array to string
            skills_str = ','.join(skills)

            # Define values to be inserted
            values = (position, company, location, work_mode, skills_str, details)

            # Execute insert statement
            cursor.execute(insert_query, values)

            # Commit changes to the database
            conn.commit() 

        cursor.close()

    
