import requests
from lxml import html
import bs4 as bs
import urllib
import sys
# import time

listOfCollege = {
        "Department of Psychology-(211)" : '211',
        "Mata Sundri College For Women-(044)" : '044',
        "Gargi College-(024)" : '024',
        "Maharshi Valmiki College of Education-(315)" : '315',
        "Department of Social Sciences-(115)" : '115',
        "Lakshmibai College - Teaching Centre-(1310)" : '1310',
        "LAW CENTRE-I-(310)" : '310',
        "Department of Chemistry -(217)" : '217',
        "Deshbandhu College (Day)-(019)" : '019',
        "Kamla Nehru College-(034)" : '034',
        "Lady Sri Ram College For Women-(039)" : '039',
        "Shivaji College-(071)" : '071',
        "Moti Lal Nehru College (Day)-(048)" : '048',
        "Ramanujan College-(020)" : '020',
        "Bhagini Nivedita College (Teaching Centre)-(1317)" : '1317',
        "Department of Germanic and Romance Studies-(204)" : '204',
        "Zakir Husain College (Eve)-(086)" : '086',
        "Satyawati College (Eve)-(063)" : '063',
        "Sri Guru Gobind Singh College Of Commerce - Teaching Centre-(1312)" : '1312',
        "Department of Hindi-(205)" : '205',
        "Department of Punjabi-(212)" : '212',
        "Department of Sociology-(230)" : '230',
        "Sri Venkateswara College-(079)" : '079',
        "Department of Microbiology-(253)" : '253',
        "P.G.D.A.V. College (Eve)-(054)" : '054',
        "Bharati College-(008)" : '008',
        "Department of Geology-(219)" : '219',
        "University of Delhi-(100)" : '100',
        "Shyama Prasad Mukherjee College-(075)" : '075',
        "I.P.College For Women-(029)" : '029',
        "Mata Sundri College For Women - Teaching Centre-(1303)" : '1303',
        "Department of Linguistics -(207)" : '207',
        "Non Collegiate Women Education Board (NCWEB)-(307)" : '307',
        "Jesus & Mary College - Teaching Centre-(1308)" : '1308',
        "Department of Anthropology -(215)" : '215',
        "Department of OperationalResearch -(236)" : '236',
        "Rajdhani College-(055)" : '055',
        "Department of Urdu-(214)" : '214',
        "Keshav Mahavidyalaya-(035)" : '035',
        "Aryabhatta College [Formerly Ram Lal Anand College (Evening)]-(059)" : '059',
        "Department of East Asian Studies -(228)" : '228',
        "Shyam Lal College (Eve)-(074)" : '074',
        "College of Vocational Studies (Teaching Centre)-(1318)" : '1318',
        "Ramjas College-(056)" : '056',
        "Department of LC-I-(239)" : '239',
        "Deen Dayal Upadhyaya College-(015)" : '015',
        "Moti Lal Nehru College (Teaching Centre)-(1321)" : '1321',
        "College Of Vocational Studies-(013)" : '013',
        "Dr. Bhim Rao Ambedkar College-(010)" : '010',
        "Department of History (SDC)-(291)" : '291',
        "Department of Buddhist Studies -(202)" :'202',
        "Shaheed Bhagat Singh College (Eve)-(065)" : '065',
        "Department of English-(203)" : '203',
        "Institute Of Home Economics-(030)" : '030',
        "Delhi School of Journalism-(316)" : '316',
        "CAMPUS LAW CENTRE-(309)" : '309',
        "School of Open Learning (SOL)-(308)" : '308',
        "Faculty of Management Studies-(109)" : '109',
        "Department of Electronics -(251)" : '251',
        "Hans Raj College-(025)" : '025',
        "Department of Indira Gandhi Institute of Physical Education and Sports Science-(255)" : '255',
        "Maharaja Agrasen College - Teaching Centre-(1302)" : '1302',
        "Moti Lal Nehru College (Eve)-(049)" : '049',
        "Bhaskaracharya College of Applied Sciences-(009)" : '009',
        "Vivekananda College-(084)" : '084',
        "Shaheed Rajguru College of Applied Sciences for Women-(066)" : '066',
        "Department of Statistics -(237)" : '237',
        "Department of Economics-(227)" : '227',
        "Department of Library and Information Science-(206)" : '206',
        "Department of Faculty of Science-(114)" : '114',
        "Department of Inter-Disciplinary And Applied Sciences-(107)" : '107',
        "Sri Guru Nanak Dev Khalsa College-(069)" : '069',
        "Sri Aurobindo College (Eve)-(077)" : '077',
        "Hans Raj College - Teaching Centre-(1313)" : '1313',
        "Department of African Studies-(226)" : '226',
        "Acharya Narendra Dev College-(001)" : '001',
        "Maharaja Agrasen College-(041)" : '041',
        "Department of Bio-chemistry -(249)" : '249',
        "Department of Mathematics -(235)" : '235',
        "Satyawati College (Teaching Centre) -(1324)" : '1324',
        "Kalindi College-(033)" : '033',
        "Shyam Lal College (Day)-(073)" : '073',
        "Department of MIL& LS -(208)" : '208',
        "Department of Social Work -(233)" : '233',
        "Ram Lal Anand College (Day)-(058)" : '058',
        "Maitreyi College - Teaching Centre-(1309)" : '1309',
        "Department of Bio Medical Research -(258)" : '258',
        "Maitreyi College-(043)" : '043',
        "Department of Geography-(229)" : '229',
        "Miranda House-(047)" : '047',
        "Dr. B.R. Ambedkar (Teaching Centre)-(1316)" : '1316',
        "Bhagini Nivedita College-(007)" : '007',
        "Department of B.A (Programme Committee) Application Course-III Foundation Course-II-(290)" : '290',
        "Department of Philosophy-(210)" : '210',
        "St. Stephens College-(080)" : '080',
        "Sri Guru Gobind Singh College Of Commerce-(078)" : '078',
        "S.G.T.B. Khalsa College-(068)" : '068',
        "Department of Zoology-(223)" : '223',
        "Department of Computer Science -(234)" : '234',
        "Department of Education-(243)" : '243',
        "Daulat Ram College-(014)" : '014',
        "Department of Environmental Studies-(218)" : '218',
        "Keshav Mahavidlaya (Teaching Centre)-(1319)" : '1319',
        "Bharati College - Teaching Centre-(1307)" : '1307',
        "Department of Home Science -(220)" : '220',
        "Department of Business Economics-(248)" : '248',
        "Swami Shraddhanand College-(081)" : '081',
        "Sri Aurobindo College (Teaching Centre)-(1325)" : '1325',
        "Dyal Singh College (Eve)-(022)" : '022',
        "Delhi College Of Arts & Commerce-(016)" : '016',
        "P.G.D.A.V. College - Teaching Centre-(1311)" : '1311',
        "LAW CENTRE-II-(311)" : '311',
        "Jubilee Hall-(306)" : '306',
        "Department of Physics -(222)" : '222',
        "Aditi Mahavidyalaya-(002)" : '002',
        "Department of Genetics-(252)" : '252',
        "Hindu College-(026)" : '026',
        "Janki Devi Memorial College-(031)" : '031',
        "Shaheed Sukhdev College of Business Studies-(067)" : '067',
        "Ramanujan College (Teaching Centre)-(1323)" : '1323',
        "Department of Political Science-(232)" : '232',
        "School of Open Learning-(SOL)" : 'SOL',
        "Shyama Prasad Mukherjee College - Teaching Centre-(1306)" : '1306',
        "Sri Ram College Of Commerce-(072)" : '072',
        "Aditi Mahavidhlaya (Teaching Centre)-(1314)" : '1314',
        "P.G.D.A.V. College (Day)-(053)" : '053',
        "Sri Aurobindo College (Day)-(076)" : '076',
        "Zakir Husain Delhi College (Day)-(085)" : '085',
        "Department of Sanskrit-(213)" : '213',
        "Lakshmibai College-(040)" : '040',
        "Department of Persian-(209)" : '209',
        "Durgabai Deshmukh College of Special Education (Visual Impairment)-(314)" : '314',
        "Aryabhatta College (Teaching Centre) -(1315)" : '1315',
        "Vivekananda College - Teaching Centre-(1301)" : '1301',
        "Janki Devi Memorial College - Teaching Centre-(1304)" : '1304',
        "Lady Irwin College-(038)" : '038',
        "Department of CLC-(238)" : '238',
        "Atma Ram Sanatan Dharam College-(003)" : '003',
        "Department of ARABIC-(201)" : '201',
        "Department of Botany -(216)" : '216',
        "Satyawati College (Day)-(062)" : '062',
        "Jesus & Mary College-(032)" : '032',
        "Kalindi College - Teaching Centre-(1305)" : '1305',
        "Kirori Mal College-(036)" : '036',
        "Miranda House (Teaching Centre)-(1320)" : '1320',
        "Department of History-(231)" : '231',
        "Dyal Singh College (Day)-(021)" : '021',
        "Department of Music-(240)" : '240',
        "Cluster Innovation Centre-(312)" : '312',
        "Department of Adult Education -(225)" : '225',
        "Department of Faculty of Applied Social Sciences & Humanities-(101)" : '101',
        "Shaheed Bhagat Singh College (Day)-(064)" : '064',
        "Rajdhani College (Teaching Centre)-(1322)" : '1322',
        "Department of Commerce-(241)" : '241',
        "Indira Gandhi Institute of Phy. Edu. & Sports Sciences-(028)" : '028'
}

class base:
    BASE_URL = "http://duexam2.du.ac.in/RSLT_ND2017/Students/Combine_GradeCard.aspx"

    session_requests = requests.session()
    payload = {}
    record = {}


    def __init__(self,
                 college='',
                 examtype='Semester',
                 examflag='CBCS',
                 stream='ART',
                 course='101',
                 part='I',
                 sem='I',
                 txtrollno='17041101001',
                 txtname='SHUBHAM KUMAR YADAV'):

        self.default = '<-----Select----->'  # DO NOT CHANGE THIS PROPERTY
        self.ddlcollege = college
        self.ddlexamtype = examtype
        self.ddlexamflag = examflag
        self.ddlstream = stream
        self.ddlcourse = course
        self.ddlpart = part
        self.ddlsem = sem
        self.txtrollno = txtrollno
        self.txtname = txtname
        self.btnsearch = 'Print Score Cart/Transcript'  # DO NOT CHANGE THIS PROPERTY

    def connect(self):
        return self.session_requests.post(self.BASE_URL, data=self.payload, headers=dict(referer=self.BASE_URL))
        # pass

        # __EVENTTARGET, ddlcollege, ddlexamtype, ddlexamflag, ddlstream, ddlcourse, ddlpart, ddlsem, txtrollno, txtname
    def load(self, target, *kargs):
        tree = html.fromstring(self.connect().text)
        authenticity_token = list(set(tree.xpath("//input[@name='__VIEWSTATE']/@value")))[0]
        authenticity_token1 = list(set(tree.xpath("//input[@name='__EVENTVALIDATION']/@value")))[0]
        self.payload["__VIEWSTATE"] = authenticity_token
        self.payload["__EVENTVALIDATION"] = authenticity_token1
        self.payload["__EVENTARGUMENT"] = ''
        self.payload["__LASTFOCUS"] = ''
        self.payload["__EVENTTARGET"] = target

        for arg in kargs:
            if arg == 'ddlcollege':
                self.payload[arg] = self.ddlcollege
            elif arg == 'ddlexamtype':
                self.payload[arg] = self.ddlexamtype
            elif arg == 'ddlexamflag':
                self.payload[arg] = self.ddlexamflag
            elif arg == 'ddlstream':
                self.payload[arg] = self.ddlstream
            elif arg == 'ddlcourse':
                self.payload[arg] = self.ddlcourse
            elif arg == 'ddlpart':
                self.payload[arg] = self.ddlpart
            elif arg == 'ddlsem':
                self.payload[arg] = self.ddlsem
            elif arg == 'txtrollno':
                self.payload[arg] = self.txtrollno
            elif arg == 'txtname':
                self.payload[arg] = self.txtname
            elif arg == 'btnsearch':
                self.payload[arg] = self.btnsearch
            else:
                print 'wrong keyword argument passed!'

    def show(self):
        print '*' * 20
        for w in self.payload:
            print w, ':', self.payload[w]

    def scrap(self, source, *ids):
        # CONTENT SCRAPING
        # TABLE -> (all)TR -> TD -> SPAN (WITH SPECIFIC IDs AND CLASSes)
        soup = bs.BeautifulSoup(source, 'lxml')
        # print soup.text
        table_body = soup.find('table')
        rows = table_body.find_all('tr')
        for row in rows:
            if row:
                cols = row.find('td')
                for id in ids:
                    try:
                        var = cols.find('span', {'id': id, 'class': 'lblsmall'})
                    except AttributeError:
                        pass
                    if var:
                        self.record[id] = var.text.strip().encode("utf-8")
                        # print var.text.strip().encode("utf-8")

    def check(self, source):
        soup = bs.BeautifulSoup(source, 'lxml')
        try:
            msg = soup.find('span', {'id': 'lblmsg', 'class': 'lbl'})
            if 'Sorry' in msg.text.strip().encode("utf-8"):
                print msg.text.strip().encode("utf-8")
                print ''
                return False
            else:
                return True
        except AttributeError:
            return True

    def tablescrap(self, source, id):
        soup = bs.BeautifulSoup(source, 'lxml')
        # DIV -> TABLE -> (all)TR -> (all)TH/(all)TD
        div = soup.find('div')
        table_body = div.find('table')
        rows = table_body.find_all('tr')
        for row in rows:
            if row:
                colsth = row.find_all('th')
                colsth = [x.text.strip().encode("utf-8") for x in colsth]
                colstd = row.find_all('td')
                colstd = [x.text.strip().encode("utf-8") for x in colstd]
                if colsth:
                    print colsth
                if colstd:
                    print colstd

        # TABLE (WITH SPECIFIC ID) -> (all)TR -> (all)TH/(all)TD
        table_body = soup.find('table', {'id': id})
        rows = table_body.find_all('tr')
        record3 = []
        for row in rows:
            if row:
                colsth = row.find_all('th')
                colsth = [x.text.strip().encode("utf-8") for x in colsth]
                colstd = row.find_all('td')
                colstd = [x.text.strip().encode("utf-8") for x in colstd]
                if colsth:
                    print colsth
                if colstd:
                    print colstd

o = base(college='041',
         examtype='Semester',
         examflag='CBCS',
         stream='ART',
         course='101',
         part='I',
         sem='I',
         txtrollno='17041101003',
         txtname='ABDUL SAQIB KHAN SIDDIQUI')
o.payload = {}
o.connect()
o.load('ddlexamtype', 'ddlcollege', 'ddlexamtype', 'ddlstream', 'txtrollno', 'txtname')
o.load('ddlexamflag', 'ddlcollege', 'ddlexamtype', 'ddlexamflag', 'ddlstream', 'txtrollno', 'txtname')
o.load('ddlstream', 'ddlcollege', 'ddlexamtype', 'ddlexamflag', 'ddlstream', 'ddlpart', 'txtrollno', 'txtname')
o.load('ddlcourse', 'ddlcollege', 'ddlexamtype', 'ddlexamflag', 'ddlstream', 'ddlcourse', 'ddlpart', 'txtrollno', 'txtname')
o.load('ddlpart', 'ddlcollege', 'ddlexamtype', 'ddlexamflag', 'ddlstream', 'ddlcourse', 'ddlpart', 'txtrollno', 'txtname')
o.load('', 'ddlcollege', 'ddlexamtype', 'ddlexamflag', 'ddlstream', 'ddlcourse', 'ddlpart', 'ddlsem', 'txtrollno', 'txtname', 'btnsearch')
source = o.connect()
# print source
source.encoding = 'ISO-8859-1'
source = str(source.content)
if o.check(source):
    o.scrap(source, 'lblrollno', 'lblname', 'lblcourse', 'lblsem', 'lblcollege', 'lbleno')
    o.tablescrap(source, 'gv_sgpa')
    sys.exit()
# __EVENTTARGET, ddlcollege, ddlexamtype, ddlexamflag, ddlstream, ddlcourse, ddlpart, ddlsem, txtrollno, txtname
for index,i in enumerate(listOfCollege):
    print index+1,': Trying on', i
    ob = base(college=listOfCollege[i],
             examtype='Semester',
             examflag='CBCS',
             stream='ART',
             course='101',
             part='I',
             sem='I',
             txtrollno='17041101002',
             txtname='AAYUSH SRIVASTAV')
    ob.payload = {}
    ob.connect()
    ob.load('ddlexamtype', 'ddlcollege', 'ddlexamtype', 'ddlstream', 'txtrollno', 'txtname')
    ob.load('ddlexamflag', 'ddlcollege', 'ddlexamtype', 'ddlexamflag', 'ddlstream', 'txtrollno', 'txtname')
    ob.load('ddlstream', 'ddlcollege', 'ddlexamtype', 'ddlexamflag', 'ddlstream', 'ddlpart', 'txtrollno', 'txtname')
    ob.load('ddlcourse', 'ddlcollege', 'ddlexamtype', 'ddlexamflag', 'ddlstream', 'ddlcourse', 'ddlpart', 'txtrollno', 'txtname')
    ob.load('ddlpart', 'ddlcollege', 'ddlexamtype', 'ddlexamflag', 'ddlstream', 'ddlcourse', 'ddlpart', 'txtrollno', 'txtname')
    ob.load('', 'ddlcollege', 'ddlexamtype', 'ddlexamflag', 'ddlstream', 'ddlcourse', 'ddlpart', 'ddlsem', 'txtrollno', 'txtname', 'btnsearch')
    source = ob.connect()
    # print source
    source.encoding = 'ISO-8859-1'
    source = str(source.content)
    if ob.check(source):
        ob.scrap(source, 'lblrollno', 'lblname', 'lblcourse', 'lblsem', 'lblcollege', 'lbleno')
        ob.tablescrap(source, 'gv_sgpa')
        break
    # if (index+1)%5 == 0:
        # print 'TAKING A BREAK OF 10 SEC\n'
        # time.sleep(10)
