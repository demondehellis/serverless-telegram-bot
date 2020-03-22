import json
from src.encoders import CustomJsonEncoder
from src.db_wrapper import DBWrapper

class Settings():
    """Settings wrapper"""
    def __init__(self, table):
        
        self.table = table
        self.db = DBWrapper(table)
    
    def get(self, section_name, default = None):
        
        section = self.db.get(section_name, default)
        return section

    def set(self, section_name, section = None):

        section['key'] = section_name
        result = self.db.put(section_name, section)
        return result
