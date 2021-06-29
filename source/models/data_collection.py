# python imports
import datetime
import jdatetime

# flask imports
from flask import jsonify

# project imports
from extensions import db


# TODO remove redundant jsonified property


class UsedVoucher(db.Model):
    __tablename__ = 'voucher_used'

    id = db.Column(db.BigInteger, primary_key=True)
    sold_create_date = db.Column(db.DateTime)
    serial_number = db.Column(db.String(100))
    msisdn = db.Column(db.String(100))
    used_date = db.Column(db.DateTime ,index=True)
    sold_date = db.Column(db.DateTime ,index=True)
    provisioned_voucher_group = db.Column(db.String(100))

class p2pTrans(db.Model):
    __tablename__ = 'p2p_trans'

    id = db.Column(db.BigInteger, primary_key=True)
    msisdn_nsk = db.Column(db.String(100))
    origin_msisdn = db.Column(db.String(100))
    amount = db.Column(db.Integer)
    transaction_date = db.Column(db.DateTime ,index=True)


