from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError, ContentTooShortError
import bs4

class BaseScrapper():
    
    '''Base class used to access webpages using Request'''
    
    def __init__(self, webpage):
        self._webpage = webpage
        self._soup = self.get_webpage()
        
    def get_webpage(self):
        
        ''' Returns the html of a given webpage'''
        
        try:
            req = Request(self._webpage)
            webpage = urlopen(req, timeout=30).read()
            soup = bs4.BeautifulSoup(webpage, "html.parser")
            
            return soup
        
        except URLError as urlerror:
            return None
        except HTTPError as httperror:
            return None
        except ContentTooShortError as ctserror:
            return None
        except Exception as error:
            return None
            
