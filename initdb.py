#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import *
from settings import *

l1 = Location(alias="work", address=WORK_ADDRESS)
l2 = Location(alias="home", address=HOME_ADDRESS)

db.session.add(l1)
db.session.add(l2)
db.session.commit()
