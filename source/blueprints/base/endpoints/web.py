# -*- coding: utf-8 -*-


from flask import Blueprint, render_template, request, redirect, json, make_response, session

from flask import flash, url_for, g
from models.user import LoginForm
from flask_login import LoginManager
from application import app, login_manager
from flask_login import current_user, login_user, logout_user, login_required
from flask_simpleldap import LDAP
import base64
from flask_sqlalchemy import SQLAlchemy
import time

from sqlalchemy import func, text
from sqlalchemy.sql import label

db = SQLAlchemy(app)

import ldap as l

# from models.frm_db import Frmdb
from models.data_collection import UsedVoucher, p2pTrans
from datetime import datetime

# web = Blueprint('base.web', __name__, url_prefix='', template_folder='templates')
web = Blueprint('base.web', __name__, url_prefix='', template_folder='../templates/eliteadmin-colors')


def get_user_info():
    title = session['title']
    desplayname = session['desplayname']
    department = session['department']
    thumbnailPhoto = session['thumbnailPhoto']
    return title, desplayname, department, thumbnailPhoto


@web.before_request
def get_current_user():
    print "-----------------------"
    print current_user

    g.user = None
    if 'user_id' in session:
        # This is where you'd query your database to get the user info.
        g.user = {}
        # Create a global with the LDAP groups the user is a member of.
        g.ldap_groups = ldap.get_user_groups(user=session['user_id'])


@login_manager.user_loader
def user_loader(id):
    # return User.query.get(int(id))
    # return User.query.get(id)
    pass


ldap = LDAP(app)

from pprint import pprint

import csv


def printdicttofile(dict):
    w = csv.writer(open("/media/storage/output.csv", "w"))
    for key, val in dict.items():
        w.writerow([key, val])


# def laod_data_to

@web.route('/login', methods=['GET', 'POST'])
def login():
    if g.user:
        pprint(g.user)
        return redirect(url_for('base.web.index'))

    form = LoginForm(request.form)
    print "<<<<<<<<<<<<<<<<<<<<<<<<<<"
    # print form.validate()
    # and form.validate()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        username = username.split("@")[0] + '@mtnirancell.ir'

        test = ldap.bind_user(username, password)

        if test is None or password == '':
            return render_template('login.html', form=form)
            # return 'Invalid credentials'
        else:
            userinfo = ldap.get_object_details(username)

            session['user_id'] = request.form['username']
            session['title'] = userinfo['title']
            session['department'] = userinfo['department']
            session['desplayname'] = userinfo['displayName']
            session['thumbnailPhoto'] = base64.b64encode(userinfo['thumbnailPhoto'][0])

            return redirect(url_for('base.web.index'))

    return render_template('login.html', form=form)


@web.route('/logout')
@ldap.login_required
def logout():
    logout_user()
    session.pop('user_id', None)
    return redirect(url_for('base.web.login'))


@web.route('/')
@ldap.login_required
def index():
    title, desplayname, department, thumbnailPhoto = get_user_info()

    print title
    print department
    print desplayname
    return render_template('index.html', title=title, department=department, desplayname=desplayname,
                           thumbnailPhoto=thumbnailPhoto)

import operator

@web.route('/simc', methods=['GET', 'POST'])
@ldap.login_required
def simc():
    #TODO its temperory change it to fetch from DB ASAP
    f = open('/media/storage/data/report/simc_before_activation.csv',"r")
    selectall = f.readlines()
    f.close()

    dict = {}
    for i in selectall:
        try:
            line = i.split(",")

            msisdn = line[0].strip().strip("\"")
            activation_date = line[1].split(" ")[0].strip().strip("\"")
            user_name = line[2].strip().strip("\"")
            change_of_ownership_date = line[3].split(" ")[0].strip().strip("\"")

            cow_date = datetime.strptime(change_of_ownership_date, "%m/%d/%Y")
            act_dt = datetime.strptime(activation_date, "%m/%d/%Y")
            delta = act_dt - cow_date

            if delta.days > 0:
                dict[msisdn] = [msisdn,user_name,activation_date,change_of_ownership_date,delta.days]

        except:
            pass
    dict = sorted(dict.values(), key=operator.itemgetter(4), reverse=False)
    result = ''
    for el in dict:
        result += el[0] + "," + el[1] + "," + el[2] + "," + el[3] + "," + str(el[4]) + "," + '\n'
    return result



@web.route('/regperday', methods=['GET', 'POST'])
@ldap.login_required
def regperday():
    # TODO its temperory change it to fetch from DB ASAP
    f = open('/media/storage/data/report/reg_trend_100.csv',"r")
    selectall = f.readlines()
    f.close()

    result = ''
    for i in selectall:
        try:
            line = i.split(",")

            dealer_id = line[0].strip().strip("\"")
            count = line[1].split(" ")[0].strip().strip("\"")
            result += dealer_id+','+count+'\n'


        except:
            pass

    return result


@web.route('/regperdaytab', methods=['GET', 'POST'])
@ldap.login_required
def regperdaytab():
    # TODO its temperory change it to fetch from DB ASAP
    f = open('/media/storage/data/report/reg_trend_detail.csv',"r")
    selectall = f.readlines()
    f.close()

    rows = {}
    j = 0
    for i in selectall:
        try:
            line = i.split(",")

            dw_date_key = line[1].strip().strip("\"")
            msisdn = line[2].strip().strip("\"")
            registeration_Date_d = line[3].strip().strip("\"")
            activated_by = line[4].strip().strip("\"")
            dealer_id = line[5].strip().strip("\"")

            rows[j] = []
            rows[j].append(dw_date_key)
            rows[j].append(msisdn)
            rows[j].append(registeration_Date_d)
            rows[j].append(activated_by)
            rows[j].append(dealer_id)
            j += 1
            if j > 10000:
                break
        except:
            pass
    title, desplayname, department, thumbnailPhoto = get_user_info()
    return render_template('regperdaytab.html', title=title, department=department, desplayname=desplayname,
                           thumbnailPhoto=thumbnailPhoto, datarows=rows)


@web.route('/cowperday', methods=['GET', 'POST'])
@ldap.login_required
def cowperday():
    f = open('/media/storage/data/report/cow_trend_top100.csv',"r")
    selectall = f.readlines()
    f.close()

    result = ''
    for i in selectall:
        try:
            line = i.split(",")

            dealer_id = line[0].strip().strip("\"")
            count = line[1].split(" ")[0].strip().strip("\"")
            result += dealer_id+','+count+'\n'


        except:
            pass

    return result



@web.route('/location_based_reg', methods=['GET', 'POST'])
@ldap.login_required
def location_based_reg():
    f = open('/media/storage/data/report/location_based_reg.csv',"r")
    selectall = f.readlines()
    f.close()

    result = ''
    for i in selectall:
        try:
            line = i.split(",")

            dealer_id = line[0].strip().strip("\"")
            count = line[1].split(" ")[0].strip().strip("\"")
            result += dealer_id+','+count+'\n'

        except:
            pass

    return result


@web.route('/simctab', methods=['GET', 'POST'])
@ldap.login_required
def simctab():
    f = open('/media/storage/data/report/simc_before_activation.csv',"r")
    selectall = f.readlines()
    f.close()

    rows = {}
    j = 0
    for i in selectall:
        try:
            line = i.split(",")

            msisdn = line[0].strip().strip("\"")
            activation_date = line[1].split(" ")[0].strip().strip("\"")
            user_name = line[2].strip().strip("\"")
            change_of_ownership_date = line[3].split(" ")[0].strip().strip("\"")

            cow_date = datetime.strptime(change_of_ownership_date, "%m/%d/%Y")
            act_dt = datetime.strptime(activation_date, "%m/%d/%Y")
            delta = act_dt - cow_date

            rows[j] = []
            rows[j].append(msisdn)
            rows[j].append(activation_date)
            rows[j].append(user_name)
            rows[j].append(change_of_ownership_date)
            j += 1

        except:
            pass
    title, desplayname, department, thumbnailPhoto = get_user_info()
    return render_template('simctab.html', title=title, department=department, desplayname=desplayname,
                           thumbnailPhoto=thumbnailPhoto, datarows=rows)



@web.route('/get_mss_location_checks', methods=['GET', 'POST'])
@ldap.login_required
def get_mss_location_checks():
    f = open('/media/storage/data/report/mss_location_check_simple.csv',"r")
    selectall = f.readlines()
    f.close()
    result = ''
    for i in selectall:
        line = i.split(",")
        users = line[0].strip().strip("\"")
        count = line[1].strip().strip("\"")

        result += users + "," + count + '\n'

    return result


@web.route('/get_mss_loc_check_detail', methods=['GET', 'POST'])
@ldap.login_required
def get_mss_loc_check_detail():
    f = open('/media/storage/data/report/mss_location_checks_detail.csv',"r")
    selectall = f.readlines()
    f.close()

    rows = {}
    j = 0
    for i in selectall:
        # try:
        line = i.split(",")

        msisdn_imsi = line[0].strip().strip("\"")
        operation = line[1].strip().strip("\"")
        username = line[2].strip().strip("\"")
        start_date = line[3].strip().strip("\"")
        end_date = line[4].strip().strip("\"")
        terminal = line[5].strip().strip("\"")

        rows[j] = []
        rows[j].append(msisdn_imsi)
        rows[j].append(operation)
        rows[j].append(username)
        rows[j].append(start_date)
        rows[j].append(end_date)
        rows[j].append(terminal)
        j += 1

        # except:
        #     pass
    title, desplayname, department, thumbnailPhoto = get_user_info()
    return render_template('msslockcheck.html', title=title, department=department, desplayname=desplayname,
                           thumbnailPhoto=thumbnailPhoto, datarows=rows)

@web.route('/get_usn_location_checks', methods=['GET', 'POST'])
@ldap.login_required
def get_usn_location_checks():
    f = open('/media/storage/data/report/usn_location_check_simple.csv',"r")
    selectall = f.readlines()
    f.close()
    result = ''
    for i in selectall:
        line = i.split(",")
        users = line[0].strip().strip("\"")
        count = line[1].strip().strip("\"")

        result += users + "," + count + '\n'

    return result



@web.route('/get_usn_loc_check_detail', methods=['GET', 'POST'])
@ldap.login_required
def get_usn_loc_check_detail():
    f = open('/media/storage/data/report/usn_location_checks_detail.csv',"r")
    selectall = f.readlines()
    f.close()

    rows = {}
    j = 0
    for i in selectall:
        # try:
        line = i.split(",")

        msisdn_imsi = line[0].strip().strip("\"")
        operation = line[1].strip().strip("\"")
        username = line[2].strip().strip("\"")
        start_date = line[3].strip().strip("\"")
        end_date = line[4].strip().strip("\"")
        terminal = line[5].strip().strip("\"")

        rows[j] = []
        rows[j].append(msisdn_imsi)
        rows[j].append(operation)
        rows[j].append(username)
        rows[j].append(start_date)
        rows[j].append(end_date)
        rows[j].append(terminal)
        j += 1

        # except:
        #     pass
    title, desplayname, department, thumbnailPhoto = get_user_info()
    return render_template('usnlockcheck.html', title=title, department=department, desplayname=desplayname,
                           thumbnailPhoto=thumbnailPhoto, datarows=rows)



@web.route('/getp2p', methods=['GET', 'POST'])
@ldap.login_required
def getp2p():

    # selectall = db.session.query(p2pTrans.origin_msisdn, label('numberofrows', db.func.count(p2pTrans.id)),
    #                              label('amount', db.func.sum(p2pTrans.amount))).group_by(
    #     p2pTrans.origin_msisdn).order_by('numberofrows DESC').limit(40)

    f = open('/media/storage/data/report/p2p_top_40.csv',"r")
    selectall = f.readlines()
    f.close()

    rows_per_ms = {}
    result = ''
    for i in selectall:
        line = i.split(",")
        # date_key = str(i.date_key)
        # origin_msisdn = i.origin_msisdn
        # transaction_date = str(i.transaction_date)

        origin_msisdn = line[0].strip().strip("\"")
        count = line[2].strip().strip("\"")
        amount = line[1].strip().strip("\"")

        result += origin_msisdn + "," + count + "," + amount + '\n'
        # if rows_per_ms.get(msisdn_nsk, False) == False:
        #     rows_per_ms[msisdn_nsk] = [1, int(amount)]
        # else:
        #     rows_per_ms[msisdn_nsk][0] = rows_per_ms[msisdn_nsk][0] + 1
        #     rows_per_ms[msisdn_nsk][1] = rows_per_ms[msisdn_nsk][1] + int(amount)

    # for msisdn in rows_per_ms:
    #     result += msisdn + "," + str(rows_per_ms[msisdn][0]) + "," + str(rows_per_ms[msisdn][1]) + '\n'

    # print result
    return result


@web.route('/getvoucherused', methods=['GET', 'POST'])
@ldap.login_required
def getvoucherused():
    # selectall = UsedVoucher.query.filter(UsedVoucher.sold_date < '2017-01-01').limit(40)
    f = open('/media/storage/data/report/ppms_voucher_used_top_40.csv', "r")
    selectall = f.readlines()
    f.close()

    rows = {}
    result = ''
    j = 0
    for i in selectall:
        j += 1

        line = i.split(',')
        id = line[0]
        sold_create_date = line[1]
        serial_number = line[2]
        msisdn = line[3]
        used_date = line[4]
        sold_date = line[5]
        provisioned_voucher_group = line[6]

        rows[id] = []
        rows[id].append(sold_create_date)
        rows[id].append(serial_number)
        rows[id].append(msisdn)
        rows[id].append(used_date)
        rows[id].append(sold_date)
        rows[id].append(provisioned_voucher_group)
        used_date_dt = datetime.strptime(used_date, "%Y-%m-%d")
        sold_date_dt = datetime.strptime(sold_date, "%Y-%m-%d")
        delta = used_date_dt - sold_date_dt
        result += msisdn + ',' + serial_number + ',' + str(delta.days) + '\n'
    return result
    # return "<!DOCTYPE html> <html> <body>  <h1>My First Heading</h1>  <p>My first paragraph.</p>  </body> </html>"


@web.route('/p2ptrasfer', methods=['GET', 'POST'])
@ldap.login_required
def p2ptrasfer():
    if request.method == 'POST':
        pass

    else:
        # selectall = p2pTrans.query.limit(100)
        f = open('/media/storage/data/report/p2p_top_detail.csv', "r")
        selectall = f.readlines()
        f.close()

        rows = {}

        j = 0
        for i in selectall:
            j += 1
            line = i.split(",")
            id = line[0].strip().strip("\"")
            msisdn_nsk = line[2].strip().strip("\"")
            origin_msisdn = line[3].strip().strip("\"")
            amount = line[4].strip().strip("\"")
            transaction_date = line[5].strip().strip("\"")

            rows[id] = []
            rows[id].append(transaction_date)
            rows[id].append(origin_msisdn)
            rows[id].append(msisdn_nsk)
            rows[id].append(amount)
            if j >= 1000:
                break
        # f.close()
        title, desplayname, department, thumbnailPhoto = get_user_info()
        return render_template('p2ptrans.html', title=title, department=department, desplayname=desplayname,
                               thumbnailPhoto=thumbnailPhoto, datarows=rows)


@web.route('/usedvoucher', methods=['GET', 'POST'])
@ldap.login_required
def usedvoucher():
    if request.method == 'POST':
        pass

    else:
        f = open('/media/storage/data/report/ppms_voucher_used_detail.csv', "r")
        selectall = f.readlines()
        f.close()

        rows = {}
        j = 0
        for i in selectall:
            j += 1

            line = i.split(',')
            id = line[0]
            sold_create_date = line[1]
            serial_number = line[2]
            msisdn = line[3]
            used_date = line[4]
            sold_date = line[5]
            provisioned_voucher_group = line[6]

            rows[id] = []
            rows[id].append(sold_create_date)
            rows[id].append(serial_number)
            rows[id].append(msisdn)
            rows[id].append(used_date)
            rows[id].append(sold_date)
            rows[id].append(provisioned_voucher_group)
            used_date_dt = datetime.strptime(used_date, "%Y-%m-%d")
            sold_date_dt = datetime.strptime(sold_date, "%Y-%m-%d")

            if j > 1000:
                break

        # f.close()
        title, desplayname, department, thumbnailPhoto = get_user_info()
        return render_template('usedvoucher.html', title=title, department=department, desplayname=desplayname,
                               thumbnailPhoto=thumbnailPhoto, datarows=rows)
    # return "done"



@web.route('/invoice_rep', methods=['GET', 'POST'])
@ldap.login_required
def invoice_rep():
    f = open('/media/storage/data/report/repetetive_invoice.csv',"r")
    selectall = f.readlines()
    f.close()

    result = ''
    for i in selectall:
        try:
            line = i.split(",")

            supplier = line[0].strip().strip("\"")
            count = line[1].strip("\"")
            amount = line[2].strip().strip("\"")

            result += supplier + "," + str(count) + "," + amount + '\n'
            # result += msisdn + "," + user_name + "," + activation_date + "," + change_of_ownership_date + "," + str(
            #     delta.days) + "," + '\n'

        except:
            pass
    return result


@web.route('/report')
@ldap.login_required
def report():
    title, desplayname, department, thumbnailPhoto = get_user_info()
    return render_template('morris-chart.html', title=title, department=department, desplayname=desplayname,
                           thumbnailPhoto=thumbnailPhoto)


@web.route('/faq')
@ldap.login_required
def faq():
    title, desplayname, department, thumbnailPhoto = get_user_info()
    return render_template('faq.html', title=title, department=department, desplayname=desplayname,
                           thumbnailPhoto=thumbnailPhoto)
