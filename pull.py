import testy

def user(handle):
    """
    returns a list of users who need to be roasted
    List of dict
    """
    return {"name" : handle, 
            "bio" : testy.getBio(handle)}
