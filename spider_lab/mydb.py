# -*- coding: utf-8 -*-

import sys 
from config import db_name
from mongoengine import *
connect(db_name)
#register_connection('gter-db', 'gter')

class Data(Document):
    tid = StringField()
    application_year = StringField()
    start_term = StringField()
    profession = StringField()
    degree = StringField()
    pay = StringField()
    submission_time = StringField() 
    application_result = StringField() 
    school = StringField() 
    notice_time = StringField() 
    undergraduate_school = StringField() 
    undergraduate_school_name = StringField() 
    undergraduate_profession = StringField() 
    undergraduate_grades = StringField() 
    graduate_grade = StringField() 
    graduate_school = StringField() 
    graduate_profession = StringField() 
    graduate_grades = StringField() 
    toefl = StringField() 
    gre = StringField() 
    sub_grades = StringField() 
    other_bg = StringField() 
    
