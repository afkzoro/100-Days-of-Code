def square(user):
    """_summary_
 
    Args:
        user (_type_): _description_
 
    Raises:
        ValueError: _description_
 
    Returns:
        _type_: _description_
    """
    if user <= 0 or user > 64:
        raise ValueError("square must be between 1 and 64")
    return 2**(user - 1)
    
def total():
    """_summary_
 
    Returns:
        _type_: _description_
    """
    return 2**64 -1