# python imports
import datetime
import jdatetime

# flask imports
from flask import jsonify

# project imports
from extensions import db


# TODO remove redundant jsonified property

class Frmdb(db.Model):
    __tablename__ = 'FRM_db'

    id = db.Column(db.BigInteger, primary_key=True)
    FRA_Name = db.Column(db.String(100), index=True)
    Date_Of_Report = db.Column(db.DateTime ,index=True)
    Fraud_Risk_Category = db.Column(db.String(100) ,index=True)
    Fraud_Risk_description = db.Column(db.String(1000))
    Recommendation = db.Column(db.String(1000))
    Management_Action = db.Column(db.String(1000))
    Rating = db.Column(db.String(100) ,index=True)
    Rating1 = db.Column(db.String(100) ,index=True)
    Source = db.Column(db.String(100))
    Primary_Risk_Owner = db.Column(db.String(100))
    Mitigation_Owner_Division = db.Column(db.String(100))
    Mitigation_Owner = db.Column(db.String(100))
    Due_Date = db.Column(db.DateTime ,index=True)
    Extended_Due_Date = db.Column(db.DateTime ,index=True)
    Valid_Due_date = db.Column(db.DateTime ,index=True)
    Age_Days = db.Column(db.String(100))
    Aging_Month = db.Column(db.String(100))
    Date_Of_Implement = db.Column(db.DateTime ,index=True)
    Status = db.Column(db.String(100) ,index=True)
    Follow_up_date_and_result_Reasons_for_implementation = db.Column(db.DateTime)
    Responsible = db.Column(db.String(100) ,index=True)
    Comment_Challenges = db.Column(db.String(1000))
    Ontime_Closure = db.Column(db.String(100))
