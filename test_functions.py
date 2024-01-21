"""Test for my functions.
"""
import requests
import pandas as pd
from bs4 import BeautifulSoup
from bs4 import NavigableString

from functions import ext_ac_program, ext_purpose, ext_club_email, ext_board_emails

def test_ext_ac_program():
    
    base_url = 'https://studentorg.ucsd.edu/Home/Details/15823'
    ac_program_out = ext_ac_program(base_url)
    
    assert callable(ext_ac_program)
    assert isinstance(ac_program_out, str)
    assert ac_program_out == 'Undergraduate'

def test_ext_purpose():
    
    base_url = 'https://studentorg.ucsd.edu/Home/Details/15823'
    purpose_out = ext_purpose(base_url)

    assert isinstance(purpose_out, str)
    assert '\r\n' not in purpose_out
    assert 'ACM AI' in purpose_out
    
def test_ext_club_email():
    
    base_url = 'https://studentorg.ucsd.edu/Home/Details/15823'
    club_email_out = ext_club_email(base_url)

    assert type(club_email_out) == NavigableString 
    assert 'ai' in club_email_out
    assert '.org' in club_email_out

def test_ext_board_emails():

    base_url = 'https://studentorg.ucsd.edu/Home/Details/15823'
    board_email_list = ext_board_emails(base_url)
   
    assert callable(ext_board_emails)
    assert type(board_email_list) == list
    assert len(board_email_list) == 3
    assert board_email_list[0] == 'stao@ucsd.edu'
    
test_ext_ac_program()
test_ext_purpose()
test_ext_club_email()
test_ext_board_emails()
    

                 
    