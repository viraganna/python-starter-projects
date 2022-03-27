def get_yn(prompt, yes_values={"y", "yes"}, no_values={"n", "no"}):
    """
    Prompt for a yes or no response;
    return True for yes or False for no
    """
    while True:
        response = input(prompt).strip().lower()
        if response in yes_values:
            return True
        elif response in no_values:
            return False