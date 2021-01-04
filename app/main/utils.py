from datetime import datetime

slot_dict = {0:{9:"A", 10:"B", 11:"C", 12:"D", 14:"P", 16:"Q",23:"D"},
            1:{9:"D", 10:"E", 11:"F", 12:"G", 14:"R", 16:"S"},
            2:{9:"B", 10:"C", 11:"A", 12:"G", 14:"F"},
            3:{9:"C", 10:"A", 11:"B", 12:"E", 14:"Q", 16:"P"},
            4:{9:"E", 10:"F", 11:"D", 12:"G", 14:"S", 16:"R"}}

def get_slot(dt_object):
    """Function to return the string slot using data passed from a datetime.datetime object"""
    accessor = dt_object.hour
    day = dt_object.weekday()
    try :
        slot = slot_dict[day][accessor]
    except KeyError as e:
        return "X"
    return slot