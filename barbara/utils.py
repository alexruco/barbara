#barbara/utils.py

from urllib.parse import urlparse

def get_home_page(url: str) -> str:
    """
    Extracts the pure domain from a given URL, returning the homepage URL.
    
    Args:
        url (str): The URL to parse.
        
    Returns:
        str: The pure domain in the format "https://domain.com".
    """
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return f"{parsed_url.scheme}://{domain}" if domain else None
