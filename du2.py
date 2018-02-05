# MADE BY NIKHIL TANEJA
# STUDENT AT NORTHCAP UNIVERSITY
# EMAIL: taneja.nikhil03@gmail.com

import requests
from lxml import html
import bs4 as bs
import urllib

BASE_URL = "http://duexam2.du.ac.in/RSLT_ND2017/Students/Combine_GradeCard.aspx"

#######################################################################################
# STUDENT'S DETAILS

default = '<-----Select----->'  # DO NOT CHANGE THIS PROPERTY
ddlcollege = '026'
ddlexamtype = 'Semester'
ddlexamflag = 'CBCS'
ddlstream = 'SC'
ddlcourse = '582'
ddlpart = 'I'
ddlsem = 'I'
txtrollno = '17026582122'
txtname = 'HARSH YADAV'
btnsearch = 'Print Score Cart/Transcript'  # DO NOT CHANGE THIS PROPERTY

#######################################################################################
# FINAL RECORDS FETCHED ARE SAVED IN THESE VARIABLES

record = {}
final_record = []
grade = []

######################################################################################

session_requests = requests.session()

###
# NOTE ALL THE FORM POST DATA IS NOT BEING SENT IN A SINGLE CLICK, THATS WHY WE POSTED EACH SESSION DATA STEP BY STEP
###

# Get login csrf token
result = session_requests.get(BASE_URL)
tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='__VIEWSTATE']/@value")))[0]
authenticity_token1 = list(set(tree.xpath("//input[@name='__EVENTVALIDATION']/@value")))[0]

# Create payload
payload = {
    "__VIEWSTATE": authenticity_token,
    "__EVENTVALIDATION": authenticity_token1,
    "__EVENTTARGET": 'ddlexamtype',
    "__EVENTARGUMENT": '',
    "__LASTFOCUS": '',
    "ddlcollege": ddlcollege,
    "ddlexamtype": ddlexamtype,
    # "ddlexamflag": 'CBCS',
    "ddlstream": default,
    # "ddlcourse": '107',
    # "ddlpart": 'I',
    # "ddlsem": 'I',
    "txtrollno": '',
    "txtname": '',
    # "btnsearch": 'Print Score Cart/Transcript',
}

result = session_requests.post(BASE_URL, data=payload, headers=dict(referer=BASE_URL))

# Get login csrf token
tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='__VIEWSTATE']/@value")))[0]
authenticity_token1 = list(set(tree.xpath("//input[@name='__EVENTVALIDATION']/@value")))[0]

# Create payload
payload = {
    "__VIEWSTATE": authenticity_token,
    "__EVENTVALIDATION": authenticity_token1,
    "__EVENTTARGET": 'ddlexamflag',
    "__EVENTARGUMENT": '',
    "__LASTFOCUS": '',
    "ddlcollege": ddlcollege,
    "ddlexamtype": ddlexamtype,
    "ddlexamflag": ddlexamflag,
    "ddlstream": default,
    # "ddlcourse": '107',
    "ddlpart": default,
    # "ddlsem": 'I',
    "txtrollno": '',
    "txtname": '',
    # "btnsearch": 'Print Score Cart/Transcript',
}

result = session_requests.post(BASE_URL, data=payload, headers=dict(referer=BASE_URL))

# Get login csrf token
tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='__VIEWSTATE']/@value")))[0]
authenticity_token1 = list(set(tree.xpath("//input[@name='__EVENTVALIDATION']/@value")))[0]

# Create payload
payload = {
    "__VIEWSTATE": authenticity_token,
    "__EVENTVALIDATION": authenticity_token1,
    "__EVENTTARGET": 'ddlstream',
    "__EVENTARGUMENT": '',
    "__LASTFOCUS": '',
    "ddlcollege": ddlcollege,
    "ddlexamtype": ddlexamtype,
    "ddlexamflag": ddlexamflag,
    "ddlstream": ddlstream,
    # "ddlcourse": '107',
    "ddlpart": default,
    # "ddlsem": 'I',
    "txtrollno": '',
    "txtname": '',
    # "btnsearch": 'Print Score Cart/Transcript',
}

result = session_requests.post(BASE_URL, data=payload, headers=dict(referer=BASE_URL))

# Get login csrf token
tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='__VIEWSTATE']/@value")))[0]
authenticity_token1 = list(set(tree.xpath("//input[@name='__EVENTVALIDATION']/@value")))[0]

# Create payload
payload = {
    "__VIEWSTATE": authenticity_token,
    "__EVENTVALIDATION": authenticity_token1,
    "__EVENTTARGET": 'ddlcourse',
    "__EVENTARGUMENT": '',
    "__LASTFOCUS": '',
    "ddlcollege": ddlcollege,
    "ddlexamtype": ddlexamtype,
    "ddlexamflag": ddlexamflag,
    "ddlstream": ddlstream,
    "ddlcourse": ddlcourse,
    "ddlpart": default,
    # "ddlsem": 'I',
    "txtrollno": '',
    "txtname": '',
    # "btnsearch": 'Print Score Cart/Transcript',
}

result = session_requests.post(BASE_URL, data=payload, headers=dict(referer=BASE_URL))

# Get login csrf token
tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='__VIEWSTATE']/@value")))[0]
authenticity_token1 = list(set(tree.xpath("//input[@name='__EVENTVALIDATION']/@value")))[0]

# Create payload
payload = {
    "__VIEWSTATE": authenticity_token,
    "__EVENTVALIDATION": authenticity_token1,
    "__EVENTTARGET": 'ddlpart',
    "__EVENTARGUMENT": '',
    "__LASTFOCUS": '',
    "ddlcollege": ddlcollege,
    "ddlexamtype": ddlexamtype,
    "ddlexamflag": ddlexamflag,
    "ddlstream": ddlstream,
    "ddlcourse": ddlcourse,
    "ddlpart": ddlpart,
    # "ddlsem": 'I',
    "txtrollno": '',
    "txtname": '',
    # "btnsearch": 'Print Score Cart/Transcript',
}

result = session_requests.post(BASE_URL, data=payload, headers=dict(referer=BASE_URL))

# Get login csrf token
tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='__VIEWSTATE']/@value")))[0]
authenticity_token1 = list(set(tree.xpath("//input[@name='__EVENTVALIDATION']/@value")))[0]

# Create payload
payload = {
    "__VIEWSTATE": authenticity_token,
    "__EVENTVALIDATION": authenticity_token1,
    "__EVENTTARGET": '',
    "__EVENTARGUMENT": '',
    "__LASTFOCUS": '',
    "ddlcollege": ddlcollege,
    "ddlexamtype": ddlexamtype,
    "ddlexamflag": ddlexamflag,
    "ddlstream": ddlstream,
    "ddlcourse": ddlcourse,
    "ddlpart": ddlpart,
    "ddlsem": ddlsem,
    "txtrollno": txtrollno,
    "txtname": txtname,
    "btnsearch": btnsearch,
}

result = session_requests.post(BASE_URL, data=payload, headers=dict(referer=BASE_URL))

# ISO-8859-1 is the default character in HTML 4.01.
# TO CONVERT RETURNED SESSION TO HTML
result.encoding = 'ISO-8859-1'

source = str(result.content)

# CONTENT SCRAPING
# TABLE -> (all)TR -> TD -> SPAN (WITH SPECIFIC IDs AND CLASSes)
soup = bs.BeautifulSoup(source, 'lxml')
table_body = soup.find('table')
rows = table_body.find_all('tr')
for row in rows:
    if row:
        cols = row.find('td')
        # EXAM ROLL NO.
        try:
            exam_roll = cols.find('span', {'id': "lblrollno", 'class': 'lblsmall'})
        except AttributeError:
            pass
        if exam_roll:
            record['exam_roll'] = exam_roll.text.strip().encode("utf-8")
            # print exam_roll.text.strip().encode("utf-8")

        # NAME
        try:
            name = cols.find('span', {'id': "lblname", 'class': 'lblsmall'})
        except AttributeError:
            pass
        if name:
            record['name'] = name.text.strip().encode("utf-8")
            # print name.text.strip().encode("utf-8")

        # COURSE NAME
        try:
            course = cols.find('span', {'id': "lblcourse", 'class': 'lblsmall'})
        except AttributeError:
            pass
        if course:
            record['course'] = course.text.strip().encode("utf-8")
            # print course.text.strip().encode("utf-8")

        # SEMESTER NUMBER
        try:
            sem = cols.find('span', {'id': "lblsem", 'class': 'lblsmall'})
        except AttributeError:
            pass
        if sem:
            record['sem'] = sem.text.strip().encode("utf-8")
            # print sem.text.strip().encode("utf-8")

        # COLLEGE NAME
        try:
            clg_name = cols.find('span', {'id': "lblcollege", 'class': 'lblsmall'})
        except AttributeError:
            pass
        if clg_name:
            record['clg_name'] = clg_name.text.strip().encode("utf-8")
            # print clg_name.text.strip().encode("utf-8")

        # ENROLLMENT NO.
        try:
            eno = cols.find('span', {'id': "lbleno", 'class': 'lblsmall'})
        except AttributeError:
            pass
        if eno:
            record['eno'] = eno.text.strip().encode("utf-8")

# DIV -> TABLE -> (all)TR -> (all)TH
div = soup.find('div')
table_body = div.find('table')
rows = table_body.find_all('tr')
record2 = []
for row in rows:
    if row:
        cols = row.find_all('th')
        cols = [x.text.strip().encode("utf-8") for x in cols]
        if cols:
            if record2:
                pass
            else:
                record2 = cols
            # print cols

# DIV -> TABLE -> (all)TR -> (all)TR
div = soup.find('div')
table_body = div.find('table')
rows = table_body.find_all('tr')

for row in rows:
    d = {}
    if row:
        cols = row.find_all('td')
        cols = [x.text.strip().encode('utf-8') for x in cols]
        if cols:
            i = 0
            for j in cols:
                d[record2[i]] = j
                i += 1
            final_record.append(d)

# TABLE (WITH SPECIFIC ID) -> (all)TR -> (all)TH
table_body = soup.find('table', {'id': 'gv_sgpa'})
rows = table_body.find_all('tr')
record3 = []
for row in rows:
    if row:
        cols = row.find_all('th')
        cols = [x.text.strip().encode("utf-8") for x in cols]
        if cols:
            if record3:
                pass
            else:
                record3 = cols
            # print cols
# TABLE (WITH SPECIFIC ID) -> (all)TR -> (all)TD
table_body = soup.find('table', {'id': 'gv_sgpa'})
rows = table_body.find_all('tr')

for row in rows:
    info = {}
    if row:
        cols = row.find_all('td')
        cols = [x.text.strip().encode('utf-8') for x in cols]
        if cols:
            i = 0
            for j in cols:
                info[record3[i]] = j
                i += 1
            grade.append(info)
            # print info

###
# DISPLAYING CONTENT
###

# STUDENT'S DETAILS
for i in record:
    print i, ':', record[i]
print ''

# SUBJECT WISE MARKS/CREDITS
for i in final_record:
    for j in i:
        print j, ':', i[j]
    print ''

# TOTAL CGPA/SGPA/CREDITS
for i in grade:
    for j in i:
        print j, ':', i[j]
    print ''
