#!/usr/bin/env python3
""" class that inherits from class BaseModel"""

from models.basemodel import BaseModel


class Review(BaseModel):
    """has public class attributes place id, user id and text"""
    place_id = ""
    user_id = ""
    text = ""
