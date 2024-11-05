#barbara/personas_handler.py

import sqlite3
from ai_handler import is_persona


def get_leads_with_unknown_persona():
    conn = sqlite3.connect('db_leads.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id_lead, homepage_lead FROM tb_leads WHERE (is_persona IS NULL OR is_persona = "")  AND (site_description IS NOT NULL AND site_description <> "")')
    leads = cursor.fetchall()
    conn.close()
    return leads  # Returns a list of tuples (id_lead, homepage_lead)

def update_is_persona_by_id(id_lead, is_persona_value):
    conn = sqlite3.connect('db_leads.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE tb_leads
        SET is_persona = ?
        WHERE id_lead = ?
    ''', (is_persona_value, id_lead))
    conn.commit()
    conn.close()
    print(f"Updated is_persona for id_lead {id_lead} to {is_persona_value}")

def process_leads_and_update_persona():
    leads = get_leads_with_unknown_persona()
    for id_lead, homepage_lead in leads:
        print(f"Processing id_lead {id_lead}: {homepage_lead}")
        persona_result = is_persona(homepage_lead)
        if persona_result is not None:
            # Convert boolean to integer for SQLite (True -> 1, False -> 0)
            is_persona_value = int(persona_result)
            update_is_persona_by_id(id_lead, is_persona_value)
        else:
            print(f"Could not determine is_persona for id_lead {id_lead} ({homepage_lead})")
            