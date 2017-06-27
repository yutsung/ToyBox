"""
"""

class Account:
    def __init__(self, username, passwd):
        self.username = username
        self.passwd = passwd

def load_account():
    account = Account("your username", "your passwd")
    return account