import string, random
from database import Database

class Shortener:
    def __init__(self):
        self.database = Database()
    
    def cleanup(self):
        self.database.close()

    def generate_key(self, url):
        key = "".join(random.choices(string.digits, k=random.randint(4, 10)))
        while not self.check_unique(key):
            key = "".join(random.choices(string.digits, k=random.randint(4, 10)))
        self.add_to_database(key, url)
        return key
    
    def check_unique(self, key):
        search = self.database.get(key)
        return not bool(search)
    
    def add_to_database(self, key, url):
        self.database.insert(key, url)
    
    def gel(self, user_key):
        key = ""
        for char in user_key:
            if char in string.digits:
                key += char
        return key

    def get_url(self, key):
        search = self.database.get(self.gel(key))
        if search:
            return search[0][1]
        return None