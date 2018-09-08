#!/usr/bin/env python3
# -*- coding: iso-8859-15 -*-

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from tabledef import *

engine = ""

try:
   from settings_dump import *
except ImportError:
   pass

# create a Session
Session = sessionmaker(bind=engine)
session: Session = Session()

# Create object
for flaredb in session.query(flaredb).filter(flaredb.ship_name == 'Essin'):
        print (flaredb.ship_name, flaredb.dmg_type, flaredb.dmg)

