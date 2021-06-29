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

    # @property
    # def jsonified(self):
    #     return jsonify(self.json)
    #
    # @property
    # def json(self):
    #     created_fa = jdatetime.date.fromgregorian(day=self.created.day, month=self.created.month,
    #                                               year=self.created.year)
    #     return {
    #         'id': str(self.id),
    #         'name': self.name,
    #         'name_en': self.name_en,
    #         'description': self.description,
    #         'product_type': self.product_type,
    #         'image_big': self.image_big,
    #         'image_small': self.image_small,
    #         'price': str(self.price),
    #         'price_off': str(self.price_off),
    #         'status': self.status,
    #         'created': self.created.strftime('%Y/%m/%d %H:%M:%S'),
    #         'active': str(self.active),
    #         'created_fa': str(self.created.strftime('%H:%M ') + created_fa.strftime('%Y/%m/%d'))
    #     }


# class OfferRules(db.Model):
#     __tablename__ = 'offer_rules'
#
#     id = db.Column(db.BigInteger, primary_key=True)
#     offer_type = db.Column(db.String(50), index=True)  # can be location, bundle, coupon
#     agent_type = db.Column(db.String(50), index=True)  # can be Dealer, Service Center MTNI connect
#
#     start_date = db.Column(db.DateTime)
#     end_date = db.Column(db.DateTime)
#
#     product_id = db.Column(db.BigInteger, db.ForeignKey('product.id'), nullable=False, index=True)
#
#     # if a valid offer exists these prices will be used for the product
#     price = db.Column(db.Float, default=0)
#     dealer_price = db.Column(db.Float, default=0)
#
#     # offer_type == location
#     city = db.Column(db.String(100), index=True)
#     province = db.Column(db.String(100), index=True)
#
#     # offer_type == bundle
#
#     # first linked product
#     first_linked_product_id = db.Column(db.BigInteger, db.ForeignKey('product.id'), index=True)
#     first_linked_price = db.Column(db.Float, default=0)
#     first_linked_dealer_price = db.Column(db.Float, default=0)
#
#     # second linked product
#     second_linked_product_id = db.Column(db.BigInteger, db.ForeignKey('product.id'), index=True)
#     second_linked_price = db.Column(db.Float, default=0)
#     second_linked_dealer_price = db.Column(db.Float, default=0)
#
#     created = db.Column(db.DateTime, default=datetime.datetime.now)
#     modified = db.Column(db.DateTime)
#     status = db.Column(db.String(50), index=True)