from deta import Deta
import os
from dotenv import load_dotenv


load_dotenv(".env")

DETA_KEY = os.getenv("DETA_KEY")

DETA_KEY2 = os.getenv("DETA_KEY2")


deta = Deta(DETA_KEY)

deta1 = Deta(DETA_KEY2)

db = deta.Base("info_db")

usrdb = deta1.Base("login_db")


# Functions related to admin page-

def insert_new_admin(username,name,password):

  return usrdb.put({"key":username,"Name":name,"Password":password})
 

def fetch_admin_details():

  res = usrdb.fetch()

  return res.items


# Functions related to home page-

def insert_values(date_t,uid,name,gender,ptype,result):

  return db.put({"Date and Time":date_t,"key":uid,"Name":name,"Gender":gender,"Person":ptype,"Personality Type":result})
 

def fetch_details():

  res = db.fetch()

  return res.items



