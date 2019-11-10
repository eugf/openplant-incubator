#!/usr/env/bin python3

import os
import time
from models import schema
from sqlalchemy import create_engine
from util import get_connection_string


engine = create_engine(get_connection_string(), echo=True)
time.sleep(30)
schema.Base.metadata.create_all(bind=engine)