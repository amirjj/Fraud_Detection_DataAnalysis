# -*- coding: utf-8 -*-

# python imports
import random
import string
import hashlib
import os

# flask imports
from flask import jsonify, current_app
from flask_mail import Message

# project imports
from extensions import mail


def random_string(N):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))

    
def random_number(N=20):
    return ''.join(random.SystemRandom().choice(string.digits) for _ in range(N))


def gen_error(error_id, error_desc):
    return jsonify({
        'error_code': str(error_id),
        'desc': str(error_desc)})


def gen_seccess(success_desc):
    return jsonify({
        'error_code': str(0),
        'desc': str(success_desc)})


def send_email(sender, recipients, subject, body, attachment=None):
    # TODO fix attachments
    msg = Message(subject,
                  sender=u'ایرانسل <noreply@irancell.ir>',
                  recipients=recipients)

    # msg.body = body
    msg.html = body

    f = open(os.path.join(current_app.root_path, 'static/img/content/irancell_logo.jpg'), 'rb')
    msg.attach('irancell_logo.jpg', 'image/jpg', f.read(),
               headers=[('Content-ID', '<irancell_logo.jpg>')]
               )
    if attachment:
        f2 = open(attachment, 'rb')
        msg.attach('invoice.pdf', 'application/pdf', f2.read())

    mail.send(msg)


def encrypt(password, salt=None):
    """Encrypts a password based on the hashing algorithm."""
    to_encrypt = password + salt
    # if salt is not None:
    #     to_encrypt += salt
    # dk = hashlib.pbkdf2_hmac('sha256', to_encrypt, salt, 100000)
    return hashlib.sha512(to_encrypt).hexdigest()
