
from email_split import email_split

def extract_email(email): 
    """ extract the email addresses from a user-friendly email address"""
    addresses = email_split(email)
    return addresses[0] if addresses else ''

print extract_email('obabawale@mgbcomputers.com')