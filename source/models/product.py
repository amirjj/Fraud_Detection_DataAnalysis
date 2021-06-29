# python imports
import datetime
import jdatetime

# flask imports
from flask import jsonify

# project imports
from extensions import db


# TODO remove redundant jsonified property

class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), index=True)
    name_en = db.Column(db.String(100), index=True)
    brief = db.Column(db.String(200))
    description = db.Column(db.String(1000))

    product_type = db.Column(db.String(50), index=True)
    customer_type = db.Column(db.String(50), index=True)

    image_big = db.Column(db.String(50))
    image_small = db.Column(db.String(50))
    price = db.Column(db.Float, default=0)

    # added by Pouria in the service version
    original_price = db.Column(db.Float, default=0)
    dealer_price = db.Column(db.Float, default=0)

    price_off = db.Column(db.Float, default=0)
    is_homepage = db.Column(db.Boolean, default=False, index=True)

    upc_code = db.Column(db.String(50), index=True)
    upc_version = db.Column(db.String(50), index=True)
    upc_type = db.Column(db.String(50), index=True)
    upc_price = db.Column(db.Float, default=0)
    upc_title = db.Column(db.String(2000), index=True)
    upc_fatitle = db.Column(db.String(2000), index=True)

    device_price = db.Column(db.Float, default=0)

    status = db.Column(db.String(50), index=True)
    active = db.Column(db.Boolean, default=True, index=True)
    deleted = db.Column(db.Boolean, default=False, index=True)
    delete_time = db.Column(db.DateTime)

    homepage_order = db.Column(db.BigInteger, index=True)

    is_multi_buy = db.Column(db.Boolean, default=False, index=True)

    is_installment = db.Column(db.Boolean, default=False, index=True)
    installment_count = db.Column(db.Integer, default=0)

    created = db.Column(db.DateTime, default=datetime.datetime.now)
    modified = db.Column(db.DateTime)

    @property
    def jsonified(self):
        return jsonify(self.json)

    @property
    def json(self):
        created_fa = jdatetime.date.fromgregorian(day=self.created.day, month=self.created.month,
                                                  year=self.created.year)
        return {
            'id': str(self.id),
            'name': self.name,
            'name_en': self.name_en,
            'description': self.description,
            'product_type': self.product_type,
            'image_big': self.image_big,
            'image_small': self.image_small,
            'price': str(self.price),
            'price_off': str(self.price_off),
            'status': self.status,
            'created': self.created.strftime('%Y/%m/%d %H:%M:%S'),
            'active': str(self.active),
            'created_fa': str(self.created.strftime('%H:%M ') + created_fa.strftime('%Y/%m/%d'))
        }


class OfferRules(db.Model):
    __tablename__ = 'offer_rules'

    id = db.Column(db.BigInteger, primary_key=True)
    offer_type = db.Column(db.String(50), index=True)  # can be location, bundle, coupon
    agent_type = db.Column(db.String(50), index=True)  # can be Dealer, Service Center MTNI connect

    # duration of the offer, obviously, merci ah!
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)

    product_id = db.Column(db.BigInteger, db.ForeignKey('product.id'), nullable=False, index=True)

    # if a valid offer exists these prices will be used for the product
    price = db.Column(db.Float, default=0)
    dealer_price = db.Column(db.Float, default=0)

    # offer_type == location
    city = db.Column(db.String(100), index=True)
    province = db.Column(db.String(100), index=True)

    # offer_type == bundle

    # first linked product
    first_linked_product_id = db.Column(db.BigInteger, db.ForeignKey('product.id'), index=True)
    first_linked_price = db.Column(db.Float, default=0)
    first_linked_dealer_price = db.Column(db.Float, default=0)

    # second linked product
    second_linked_product_id = db.Column(db.BigInteger, db.ForeignKey('product.id'), index=True)
    second_linked_price = db.Column(db.Float, default=0)
    second_linked_dealer_price = db.Column(db.Float, default=0)

    created = db.Column(db.DateTime, default=datetime.datetime.now)
    modified = db.Column(db.DateTime)
    status = db.Column(db.String(50), index=True)