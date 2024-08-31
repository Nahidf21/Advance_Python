from logger import logging

def add(a,b):
    logging.debug ("The addition operetion teking place")
    return a+b

logging.debug('The addition function is called')
logging.error("we dont get ant error")
add(10,15)

