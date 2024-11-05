#from kate import get_response
from utils import get_home_page
import random


def get_response(prompt):
    #print(f"AI response from prompt:{prompt}")
    return f"AI response from prompt:{prompt}"
    
def describe_website(home_page):
    describe_website_prompt = f"Describe this business in 50 words based on the content of the homepage as follows:{home_page}"
    return get_response(describe_website_prompt)

def check_segment(segment, website_description):
    check_segment_prompt = f"Based on this website description ({website_description}), check if the business fit to the segment:{segment}"
    return get_response(check_segment_prompt)

def get_message_body(template, website_description):
    get_message_body_prompt = f"Based on this template ({template}) and this recipient description ({website_description}), write the message body"
    return get_response(get_message_body_prompt)
    
def get_message_subject(message_body):
    get_message_subject_prompt = f"Based on this message body, write a compeling subject:{message_body}"
    return get_response(get_message_subject_prompt)
    
def provide_message_content(url, segment, template):
    home_page = get_home_page(url)
    website_description = describe_website(home_page)
    is_on_segment = check_segment(segment, website_description)
    message_body = get_message_body(template, website_description)
    message_subject = get_message_subject(message_body)
    message_content = message_body, message_subject
    return message_content

def is_persona(homepage):
    return random.choice([0, 1])

def get_site_description(homepage_content):
    return "some description"