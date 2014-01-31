from os.path import basename

def min(info):
    """Min range from parameter"""
    return info["range"].split('-')[0]

def max(info):
    """Max range from parameter"""
    return info["range"].split('-')[1]

def fallback(info):
    """Array of fallback options of parameter"""
    return info["fallback"].split(' ')

def override(info):
    """Array of override options of parameter"""
    return info["override"].split(' ')

def see(info):
    """Array of "see also" in the parameter"""
    return info["see"].split(' ')

def isenum(info):
    """Return if parameter is an enum"""
    return info["type"].startswith("enum ")

def enumval(info):
    """Return array of all enum values"""
    return info["type"].split(' ')[2:]

def enumname(info):
    """Return name of enum"""
    return info["type"].split(' ')[1]

