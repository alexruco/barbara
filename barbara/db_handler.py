# barbara/db_handler.py

# barbara/db_handler.py

import sqlite3

def create_database():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('db_leads.db')
    cursor = conn.cursor()

    # Create tb_leads table with the treated flag
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tb_leads (
            id_lead INTEGER PRIMARY KEY AUTOINCREMENT,
            homepage_lead TEXT NOT NULL UNIQUE,
            email_lead TEXT,
            site_description TEXT,
            is_persona BOOLEAN NULL,
            treated INTEGER DEFAULT 0  -- 0 = untreated, 1 = treated
        )
    ''')

    # Check if 'treated' column exists, add it if not (for backwards compatibility)
    cursor.execute("PRAGMA table_info(tb_leads)")
    columns = [col[1] for col in cursor.fetchall()]
    if 'treated' not in columns:
        cursor.execute('ALTER TABLE tb_leads ADD COLUMN treated INTEGER DEFAULT 0')

    # Create tb_emails table with only lead_id and recipient as non-null fields
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tb_emails (
            id_email INTEGER PRIMARY KEY AUTOINCREMENT,
            lead_id INTEGER NOT NULL,
            recipient TEXT NOT NULL,
            email_body TEXT NULL,
            email_subject TEXT NULL,
            email_sender TEXT NULL,
            email_sent_timestamp TIMESTAMP NULL,
            FOREIGN KEY (lead_id) REFERENCES tb_leads (id_lead) ON DELETE CASCADE
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()
        
def homepage_exists(homepage_lead):
    conn = sqlite3.connect('db_leads.db')
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM tb_leads WHERE homepage_lead = ?', (homepage_lead,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def mark_lead_as_treated(lead_id):
    """
    Mark a lead as treated after sending an email.
    """
    conn = sqlite3.connect('db_leads.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tb_leads SET treated = 1 WHERE id_lead = ?', (lead_id,))
    conn.commit()
    conn.close()