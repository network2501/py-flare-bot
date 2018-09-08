#!/usr/bin/env python3
# -*- coding: iso-8859-15 -*-


from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = "" 
try:
   from settings_table import *
except ImportError:
   pass

Base = declarative_base()

########################################################################
class flaredb(Base):
    """"""
    __tablename__ = "ships"

    class_id = Column(Integer, primary_key=True)
    ship_name: str = Column(String)
    dmg_type = Column(String)
    dmg = Column(String)
    aura = Column(String)
    zen = Column(String)

    #----------------------------------------------------------------------
    def __init__(self, ship_name, dmg_type, dmg, aura, zen):
        """"""
        self.ship_name = ship_name
        self.dmg_type = dmg_type
        self.dmg = dmg
        self.aura = aura
        self.zen = zen

# create tables
Base.metadata.create_all(engine)

