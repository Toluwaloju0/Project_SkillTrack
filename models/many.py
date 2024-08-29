#!/usr/bin/python3
"""User skills table"""

from models.base_model import Base
from sqlalchemy import Table, Column, String, ForeignKey
from sqlalchemy.orm import relationship

user_skill = Table(
    'user_skill',
    Base.metadata,
    Column(
        'user_id',
        String(60),
        ForeignKey('users.id'),
        primary_key=True),
    Column(
        'skills_id',
        String(60),
        ForeignKey('skills.id'),
        primary_key=True)
)
