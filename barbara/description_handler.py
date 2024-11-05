#barbara/description_handler.py

import sqlite3
from ai_handler import get_site_description  # We'll define this function


def get_leads_with_unknown_site_description():
    conn = sqlite3.connect('db_leads.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id_lead, homepage_lead FROM tb_leads WHERE (site_description IS NULL OR site_description = "") AND (email_lead IS NOT NULL AND email_lead <> "")')
    leads = cursor.fetchall()
    conn.close()
    return leads  # Returns a list of tuples (id_lead, homepage_lead)

def update_site_description_by_id(id_lead, site_description_value):
    conn = sqlite3.connect('db_leads.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE tb_leads
        SET site_description = ?
        WHERE id_lead = ?
    ''', (site_description_value, id_lead))
    conn.commit()
    conn.close()
    print(f"Updated site_description for id_lead {id_lead}")

def process_leads_and_update_site_description():
    leads = get_leads_with_unknown_site_description()
    for id_lead, homepage_lead in leads:
        print(f"Processing id_lead {id_lead}: {homepage_lead}")
        description = get_site_description(homepage_lead)
        if description is not None:
            update_site_description_by_id(id_lead, description)
        else:
            print(f"Could not retrieve site_description for id_lead {id_lead} ({homepage_lead})")

if __name__ == "__main__":
    process_leads_and_update_site_description()