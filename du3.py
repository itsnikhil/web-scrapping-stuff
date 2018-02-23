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
ddlstream = 'COMM'
ddlcourse = '582'
ddlpart = 'I'
ddlsem = 'I'
txtrollno = '17026582122'
txtname = 'HARSH YADAV'
btnsearch = 'Print Score Cart/Transcript'  # DO NOT CHANGE THIS PROPERTY

#######################################################################################
# FINAL RECORDS FETCHED ARE SAVED IN THESE VARIABLES

colleges = {}
courses = {}
examflag = {
    "CBCS": "CBCS",
    "UG_SEMESTER_3Y": "UG_SEMESTER_3Y",
    "UG_SEMESTER_4Y": "UG_SEMESTER_4Y",
    "PG_SEMESTER_2Y": "PG_SEMESTER_2Y",
}
stream = {
    "Arts": "ART",
    "Science": "SC",
    "Commerce": "COMM",
}
part = {
    "I": "I",
    "II": "II",
    "III": "III",
    "IV": "IV",
}
semister = {
    "I": "I",
    "II": "II",
}

#######################################################################################

session_requests = requests.session()
result = session_requests.get(BASE_URL, headers=dict(referer=BASE_URL))
result.encoding = 'ISO-8859-1'
source = str(result.content)
soup = bs.BeautifulSoup(source, 'lxml')

table_body = soup.find('table')
rows = table_body.find_all('tr')
for row in rows:
    if row:
        cols = row.find('td')
        if cols:
            select = cols.find('select', {'id': 'ddlcollege'})
            if select:
                option = select.find_all('option')
                value = [o.get('value') for o in option]
                option = [x.text.strip().encode("utf-8") for x in option]
                if option:
                    for i in range(len(option)):
                        colleges[option[i]] = value[i]

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
result.encoding = 'ISO-8859-1'
source = str(result.content)
soup = bs.BeautifulSoup(source, 'lxml')

table_body = soup.find('table')
rows = table_body.find_all('tr')
for row in rows:
    if row:
        cols = row.find('td')
        if cols:
            select = cols.find('select', {'id': 'ddlcourse'})
            if select:
                option = select.find_all('option')
                value = [o.get('value') for o in option]
                option = [x.text.strip().encode("utf-8") for x in option]
                if option:
                    for i in range(len(option)):
                        courses[option[i]] = value[i]
###
# DISPLAYING CONTENT
###

for i in colleges:
    print i, ':', colleges[i]
print ''

for i in courses:
    print i, ':', courses[i]
print ''
