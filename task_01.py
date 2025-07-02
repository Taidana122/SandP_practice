def is_palindrome(string=None):
    if not isinstance(string, str):
        if isinstance(string, (int, float)):
            string = str(string)
        else:
            return False
    if string.lower().replace(' ','').replace(',','').replace('-','').replace('!','').replace("'",'')[::-1]==string.lower().replace(' ','').replace(',','').replace('-','').replace('!','').replace("'",''):
        return True
    else:
        return False
