import requests
from lxml import html
import bs4 as bs
import urllib

BASE_URL = "http://duexam2.du.ac.in/RSLT_ND2017/Students/List_Of_Declared_Results.aspx"
URL = "http://duexam2.du.ac.in/RSLT_ND2017/Students/List_Of_Students.aspx?"

#######################################################################################
# FINAL RECORDS FETCHED ARE SAVED IN THESE VARIABLES

summary = []
record = {}
subjects = []
students = []

#######################################################################################
# DETAILS

StdType = 'REG'
ExamFlag = 'CBCS'
CourseCode = 101
CourseName = 'Department of Faculty of Applied Social Sciences & Humanities-(101)'
Part = 'I'
Sem = 'I'

#######################################################################################

session_requests = requests.session()
result = session_requests.get(BASE_URL, headers=dict(referer=BASE_URL))
result.encoding = 'ISO-8859-1'
source = str(result.content)
soup = bs.BeautifulSoup(source, 'lxml')
table_body = soup.find('table', {'id': "gvshow_ata_glance"})
rows = table_body.find_all('tr')
record2 = []
for row in rows:
    if row:
        info = {}
        values = row.find_all('th')
        if values:
            values = [x.text.strip().encode("utf-8") for x in values]
            record2 = values
            # print values
        cols = row.find_all('td')
        if cols:
            cols = [x.text.strip().encode("utf-8") for x in cols]
            i = 0
            for j in cols:
                info[record2[i]] = j
                i += 1
            summary.append(info)

target = ['gvshow_ata_glance$ctl' + str(i + 2).zfill(2) + '$btn_show_details' for i in range(12)]  # (102 to 114)

result = session_requests.get(BASE_URL)
tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='__VIEWSTATE']/@value")))[0]
authenticity_token1 = list(set(tree.xpath("//input[@name='__EVENTVALIDATION']/@value")))[0]

# Create payload
payload = {
    "__VIEWSTATE": authenticity_token,
    "__EVENTVALIDATION": authenticity_token1,
    "__EVENTTARGET": target[0],
    "__EVENTARGUMENT": '',
}

result = session_requests.post(BASE_URL, data=payload, headers=dict(referer=BASE_URL))
result.encoding = 'ISO-8859-1'
source = str(result.content)
soup = bs.BeautifulSoup(source, 'lxml')

table_body = soup.find('table', {'id': "gvshow"})
rows = table_body.find_all('tr')
record2 = []
for row in rows:
    if row:
        info = {}
        values = row.find_all('th')
        if values:
            values = [x.text.strip().encode("utf-8") for x in values]
            record2 = values
            # print values
        cols = row.find_all('td')
        if cols:
            cols = [x.text.strip().encode("utf-8") for x in cols]
            i = 0
            for j in cols:
                info[record2[i]] = j
                i += 1
            subjects.append(info)
            # print cols

d = {
    'StdType': StdType,
    'ExamFlag': ExamFlag,
    'CourseCode': CourseCode,
    'CourseName': CourseName,
    'Part': Part,
    'Sem': Sem,
}
URL += urllib.urlencode(d)

# # Get login csrf token
result = session_requests.get(URL)
result.encoding = 'ISO-8859-1'
source = str(result.content)

soup = bs.BeautifulSoup(source, 'lxml')
table_body = soup.find('table')
rows = table_body.find_all('tr')
for row in rows:
    if row:
        cols = row.find('td')
        # EXAM ROLL NO.
        try:
            exam_flag = cols.find('span', {'id': "lblexamflag", 'class': 'lbl'})
        except AttributeError:
            pass
        if exam_flag:
            record['exam_flag'] = exam_flag.text.strip().encode("utf-8")
            # print exam_roll.text.strip().encode("utf-8")

        try:
            course = cols.find('span', {'id': "lblcoursecode", 'class': 'lbl'})
        except AttributeError:
            pass
        if course:
            record['course'] = course.text.strip().encode("utf-8")
            # print exam_roll.text.strip().encode("utf-8")

        try:
            course_name = cols.find('span', {'id': "lblcoursename", 'class': 'lbl'})
        except AttributeError:
            pass
        if course_name:
            record['course_name'] = course_name.text.strip().encode("utf-8")
            # print exam_roll.text.strip().encode("utf-8")

        try:
            part = cols.find('span', {'id': "lblpart", 'class': 'lbl'})
        except AttributeError:
            pass
        if part:
            record['part'] = part.text.strip().encode("utf-8")
            # print exam_roll.text.strip().encode("utf-8")

        try:
            sem = cols.find('span', {'id': "lblsem", 'class': 'lbl'})
        except AttributeError:
            pass
        if sem:
            record['sem'] = sem.text.strip().encode("utf-8")
            # print exam_roll.text.strip().encode("utf-8")

        try:
            student_type = cols.find('span', {'id': "lblstdtype", 'class': 'lbl'})
        except AttributeError:
            pass
        if student_type:
            record['student_type'] = student_type.text.strip().encode("utf-8")
            # print exam_roll.text.strip().encode("utf-8")

soup = bs.BeautifulSoup(source, 'lxml')
table_body = soup.find('table', {'id': "gvshow"})
rows = table_body.find_all('tr')
record2 = []
for row in rows:
    if row:
        info = {}
        values = row.find_all('th')
        if values:
            values = [x.text.strip().encode("utf-8") for x in values]
            record2 = values
            # print values
        cols = row.find_all('td')
        if cols:
            cols = [x.text.strip().encode("utf-8") for x in cols]
            i = 0
            for j in cols:
                info[record2[i]] = j
                i += 1
            students.append(info)

###
# DISPLAYING CONTENT
###

# for i in summary:
#     for j in i:
#         print j, ':', i[j]
#     print ''
# for i in subjects:
#     for j in i:
#         print j, ':', i[j]
#     print ''
for i in record:
    print i, ':', record[i]
print ''
for i in students:
    for j in i:
        print j, ':', i[j]
    print ''
