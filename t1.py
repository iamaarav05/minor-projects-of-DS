from sqlalchemy import create_engine

import urllib.parse
import pandas as pd

# Your credentials
user = 'root'
pw = 'Akshay@123'
db = 'dataanalytics_db'

# Encode the password to handle the '@' symbol
safe_pw = urllib.parse.quote_plus(pw)

# Create the engine using the encoded password
engine = create_engine(f"mysql+pymysql://{user}:{safe_pw}@localhost/{db}")