#!/usr/bin/env bash
"""class that inherits from basemodel"""

from models.basemodel import BaseModel


def User(BaseModel):
    """class user that inherits from basemodel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
