#barbara/email_address_handler.py
#from aaron import get_emails_from_website #base_url, max_crawl_pages=10
import sqlite3
import time

def get_emails_from_website(homepage):
    return "joe@dee.com"

def get_leads_without_email():
    conn = sqlite3.connect('db_leads.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id_lead, homepage_lead FROM tb_leads
        WHERE (email_lead IS NULL OR email_lead = '')
        AND homepage_lead IS NOT NULL AND homepage_lead != ''
    ''')
    leads = cursor.fetchall()
    conn.close()
    return leads  # Returns a list of tuples (id_lead, homepage_lead)

def update_email_by_id(id_lead, email_value):
    conn = sqlite3.connect('db_leads.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE tb_leads
        SET email_lead = ?
        WHERE id_lead = ?
    ''', (email_value, id_lead))
    conn.commit()
    conn.close()
    print(f"Updated email_lead for id_lead {id_lead}")

def process_leads_and_update_email():
    leads = get_leads_without_email()
    for id_lead, homepage_lead in leads:
        print(f"Processing id_lead {id_lead}: {homepage_lead}")
        emails = get_emails_from_website(homepage_lead)
        print(f"Emails found: {emails}")
        print(f"Type of emails: {type(emails)}")
        if emails:
            # If emails is a string, wrap it in a list
            if isinstance(emails, str):
                emails = [emails]
            elif not isinstance(emails, list):
                print(f"Unexpected type for emails: {type(emails)}")
                continue  # Skip to the next lead
            # Now emails is a list; join them into a string
            email_value = ', '.join(emails)
            update_email_by_id(id_lead, email_value)
        else:
            print(f"No emails found for id_lead {id_lead} ({homepage_lead})")
        time.sleep(1)  # Be polite and wait 1 second between requests

if __name__ == "__main__":
    process_leads_and_update_email()
