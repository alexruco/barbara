#barbara/recipents_handler.py

from oldenburg import  get_search_results #query
from aaron import get_emails_from_website #base_url, max_crawl_pages=10
from utils import get_home_page #url
from db_handler import homepage_exists, create_database
import sqlite3

# Call the function to create the database and tables
def insert_lead(homepage_lead, email_lead='', site_description='', is_persona=None, treated=None):
    conn = sqlite3.connect('db_leads.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tb_leads (homepage_lead, email_lead, site_description, is_persona, treated)
        VALUES (?, ?, ?, ?, ?)
    ''', (homepage_lead, email_lead, site_description, is_persona, treated))
    conn.commit()
    conn.close()
    print(f"Inserted homepage: {homepage_lead} with is_persona={is_persona}")
    
def get_homepages(query):
    create_database()  # Ensure the database and tables are created
    search_results = get_search_results(query)
    home_pages = []
    for search_result in search_results:
        home_page = get_home_page(search_result)
        # Normalize the homepage URL
        home_page = home_page.split('?')[0].split('#')[0]
        if home_page not in home_pages:
            home_pages.append(home_page)
            # Check if the homepage already exists in the database
            if not homepage_exists(home_page):
                # Insert the homepage into tb_leads with is_persona as NULL
                insert_lead(
                    homepage_lead=home_page,
                    email_lead='',            # Placeholder value
                    site_description=''       # Placeholder value
                    # is_persona is omitted to default to None (NULL in the database)
                )
                print(f"Homepage added to database: {home_page}")
            else:
                print(f"Homepage already exists in database: {home_page}")
    return home_pages

def add_recipients(query):
    homepages = get_homepages(query)
    result = []
    for homepage in homepages:
        website_recipients = get_emails_from_website(base_url=homepage, max_crawl_pages=10)
        if website_recipients:
            result.append({'homepage': homepage, 'recipients': website_recipients})
    return result