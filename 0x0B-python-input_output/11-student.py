#!/usr/bin/python3
"""Define a class Student"""


class Student:
    """Defining a student profile"""
    def __init__(self, first_name, last_name, age):
        """Initialize Student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        dict_rep = self.__dict__
        dicti = {}
        if type(attrs) is list:
            for i in attrs:
                if i in dict_rep:
                    dicti.update({i: dict_rep[i]})
            return dicti
        return (dict_rep)

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        dict_rep = self.__dict__
        for i in dict_rep:
            dict_rep.update({i: json[i]})
        return (dict_rep)
