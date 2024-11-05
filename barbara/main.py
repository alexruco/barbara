# barbara/main.py

from __env_loader import load_env  
from ellis import send_message
from ai_handler import provide_message_content
from recipients_handler import get_homepages, get_search_results, add_recipients
from db_handler import create_database
from description_handler import process_leads_and_update_site_description
from email_address_handler import process_leads_and_update_email
from personas_handler import process_leads_and_update_persona
import time

# Load environment variables before any other imports
load_env()

# Create the database and give time for setup if needed
create_database()

def print_message(subject, body, recipient, sender_email):
    print("test message not sent!")

url = "https:example.com/somepage"
segment = "medium companies based in Portugal"
template = "Hello, your website could run faster!"
message_sender = "maggie@seomaggie.com"
message_recipient = "alex@ruco.pt"

def get_leads(query):
    get_homepages(query)
    process_leads_and_update_email()
    process_leads_and_update_site_description()
    process_leads_and_update_persona()
    return "leads appended to the database"

# Example usage
if __name__ == "__main__":
    query = "o que fazer em Coimbra"
    print(get_leads(query))

        
#message_body, message_subject = provide_message_content(url, segment, template)
#print(f"message_body:{message_body}")
#print(f"message_subject:{message_subject}")

#email = send_message(subject=message_subject, body=message_body, recipient=message_recipient, sender_email=message_sender)
#email = print_message(subject=message_subject, body=message_body, recipient=message_recipient, sender_email=message_sender)
#get_search_results
#get_emails_from_website

#send_email