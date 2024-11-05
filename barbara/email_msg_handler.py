# barbara/email_msg_handler.py

import sqlite3
from datetime import datetime

def get_untreated_leads():
    """
    Fetch leads from tb_leads where is_persona is True and treated is NULL or empty.
    """
    conn = sqlite3.connect('db_leads.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id_lead, homepage_lead, email_lead
        FROM tb_leads
        WHERE is_persona = 1 AND (treated IS NULL OR treated = 0)
    ''')
    leads = cursor.fetchall()
    conn.close()
    return leads

def insert_email_record(lead_id, recipient):
    """
    Insert a record into tb_emails with lead_id and recipient only.
    """
    conn = sqlite3.connect('db_leads.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tb_emails (lead_id, recipient)
        VALUES (?, ?)
    ''', (lead_id, recipient))
    conn.commit()
    conn.close()

def mark_lead_as_treated(lead_id):
    """
    Mark the lead as treated in tb_leads.
    """
    conn = sqlite3.connect('db_leads.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE tb_leads
        SET treated = 1
        WHERE id_lead = ?
    ''', (lead_id,))
    conn.commit()
    conn.close()

def process_and_insert_emails():
    """
    Process each untreated lead, insert a basic email record, and mark as treated.
    """
    leads = get_untreated_leads()
    
    for lead in leads:
        lead_id, _, email_lead = lead
        
        # Insert only the lead_id and recipient (email address) into tb_emails
        insert_email_record(lead_id, email_lead)
        
        # Mark the lead as treated
        mark_lead_as_treated(lead_id)

# Example usage
if __name__ == "__main__":
    process_and_insert_emails()