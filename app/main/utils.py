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
    ist_time = timedelta(hours =5, minutes = 30)
    dt_object += ist_time
    accessor = dt_object.hour
    day = dt_object.weekday()
    if accessor in slot_dict[day]:
        return slot_dict[day][accessor]
    else:
        return None

def is_valid_link(url):
    # Validates for google meet
    regex_google = r"https://meet.google.com/[a-z0-9\-]*"
    regex_webex = r" https://iith.webex.com/meet/"
    match_google = re.search(regex_google, str(url), re.MULTILINE)
    match_webex = re.search(regex_webex, str(url), re.MULTILINE)
    return True if (match_google or match_webex) else False

# if __name__ == "__main__":
#     print(is_valid_link("meet.google.com/iuc-xcer-zwo?pli=1&authuser=1"))
#     print(is_valid_link("https://meet.google.com/iuc-xcer-zwo"))