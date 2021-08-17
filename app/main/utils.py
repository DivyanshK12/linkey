from datetime import datetime
from datetime import timedelta
import re

slot_dict = {0:{9:"A", 10:"B", 11:"C", 12:"D", 14:"P",13:"P", 16:"Q",17:"Q"},
            1:{9:"D", 10:"E", 11:"F", 12:"G", 14:"R", 13:"R", 16:"S", 17:"S"},
            2:{9:"B", 10:"C", 11:"A", 12:"G", 14:"F", 15:"F"},
            3:{9:"C", 10:"A", 11:"B", 12:"E", 14:"Q", 15:"Q", 16:"P", 17:"P"},
            4:{9:"E", 10:"F", 11:"D", 12:"G", 14:"S", 15:"S", 16:"R", 17:"R"}}

def get_slot():
    """Function to return the string slot using data passed from a datetime.datetime object"""
    dt_object = datetime.utcnow()
    ist_time = timedelta(hours =5, minutes = 35) # Will give the link 5 minutes before the class
    dt_object += ist_time
    accessor = dt_object.hour
    day = dt_object.weekday()
    # if day in slot_dict and accessor in slot_dict[day]:
    #     return slot_dict[day][accessor]
    # else:
    #     return None
    result = slot_dict.get(day)
    return result.get(accessor) if result else result

# Validator functions
def is_valid_link(url):
    # Validates for google meet
    match_google = validate_google(url)
    match_webex = validate_webex(url)
    match_microsoft = validate_microsoft(url)
    return True if (match_google or match_webex or match_microsoft) else False

def validate_google(url):
    regex_google = r"https://meet.google.com/[a-z0-9\-]*"
    match_google = re.search(regex_google, str(url), re.MULTILINE)
    return match_google

def validate_webex(url):
    regex_webex = r"https://iithyderabad.webex.com/iithyderabad/"
    match_webex = re.search(regex_webex, str(url), re.MULTILINE)
    return match_webex

def validate_microsoft(url):
    regex_microsoft = r"https://teams.microsoft.com/dl/launcher/launcher.html"
    match_microsoft = re.search(regex_microsoft, str(url), re.MULTILINE)
    return match_microsoft