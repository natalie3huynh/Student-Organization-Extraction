"""A collection of function for doing my project."""

import requests
import pandas as pd
from bs4 import BeautifulSoup
from bs4 import NavigableString


#specified url for the ACM AI club to be passed into every function
base_url = 'https://studentorg.ucsd.edu/Home/Details/15823'

def ext_ac_program(base_url):
    
    """Extract academic program from specified club page. 
    
    Parameters
    ----------
    base_url : url
        The url to be parsed and indexed into. 
    
    Returns
    -------
    program_output : string
        The result of the indexed page content. 
    """
    page = requests.get(base_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    #locates all 'dd' html tags from page
    page_content = soup.find_all('dd') 
    
    for ac_program in page_content[4]: #finds academic program from 4th 'dd' tag
        program_output = str(ac_program)
        
    return program_output
                
def ext_purpose(base_url):
    
    """Extract purpose from specified club page. 
    
    Parameters
    ----------
    base_url : url
        The url to be parsed and indexed into 
    
    Returns
    -------
    clean_purpose : string
        The result of the indexed page content without html Carriage Return denotation. 
    """
    page = requests.get(base_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    #locates all 'dd' html tags from page to later locate purpose
    page_content = soup.find_all('dd') 
    
    for purpose in page_content[1]: #finds purpose from the 1st 'dd' tag
        purpose_output = str(purpose)
        
        #removes carriage return html characters from purpose description to make text more readable to user
        clean_purpose = purpose_output.replace('\r\n', '')
        
    return clean_purpose
                
def ext_club_email(base_url):
    
    """Extract club email from specified club page. 
    
    Parameters
    ----------
    base_url : url
        The url to be parsed and indexed into 
    
    Returns
    -------
    club_email_out : string
        The result of the indexed page content. 
    """
    page = requests.get(base_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    #locates all 'dd' html tags from page to later locate club email
    page_content = soup.find_all('dd')
    
    for club_email in page_content[5]: #finds club email from the 5th 'dd' tag
        club_email_out = club_email.string
        
    return club_email_out

def ext_board_emails(base_url):
    
    """Extract club email from specified club page. 
    
    Parameters
    ----------
    base_url : url
        The url to be parsed and indexed into 
    
    Returns
    -------
    board_email_list : list
        The list of board emails as strings. 
    """
    board_email_list = []
    
    #storing the first dataframe on the page 
    df = pd.read_html(base_url)[0]
    
    email_column = df.iloc[0:,1] #index into all of the rows containing emails and storing it into email_column
    
    for board_emails in email_column:
        if '.edu' in board_emails:
            board_email_list.append(board_emails)
            
    return board_email_list   