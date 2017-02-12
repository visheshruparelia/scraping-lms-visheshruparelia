import requests
from bs4 import BeautifulSoup
import getpass
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import sys
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def getHTML(link):
	username=raw_input("Enter Username:")
	password=getpass.getpass("Enter Password:")
	payload = {'username':username,'password':password} 
	with requests.Session() as s:
		page=s.post(link, data=payload,verify=False)
		passchecksoup=BeautifulSoup(page.content,'html.parser')
		passcheck=passchecksoup.find_all('span',class_='error')
		try:
			passcheck[0].get_text()
		except:
			req=s.get('https://lms.iiitb.ac.in/moodle/my/')
			return req
			
		if(passcheck[0].get_text()=='Invalid login, please try again'): 
			print 'Incorrect Username/Password'
			sys.exit(0)

page=getHTML('https://lms.iiitb.ac.in/moodle/login/index.php')
soup=BeautifulSoup(page.content,'html.parser')
users=soup.find_all('div',class_='user')
# // request
#due_date = soup1.find({'td',{'style':'Due date'}})
subjects=soup.find_all('div',class_='course')
dates=soup.find_all('div',class_='date')

print '\nUsers online in last five minutes:\n'
count=1
for user in users:
	print str(count)+')'+(user.get_text())	
	print '  Online Since:'+(user.a['title'])
	count+=1

count=1
print '\nUpcoming Events:\n'
for count in range(len(dates)):
	print str(count)+')'+(subjects[count].get_text())
	print '  Deadline:'+(dates[count].get_text())
	count+=1