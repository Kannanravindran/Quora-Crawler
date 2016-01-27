from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import csv

#retrieving source file
driver = webdriver.Chrome()
driver.get('http://www.quora.com')
source = driver.page_source
soup = BeautifulSoup(source.encode('utf-8','ignore'))

#login
for temp in soup.findAll("input",class_="text header_login_text_box ignore_interaction"):
	cid = temp.get("w2cid")
print 'w2cid key: ',cid
email='__w2_'+cid+'_email'
password='__w2_'+cid+'_password'
login = '__w2_'+cid+'_submit_button'
uName = driver.find_element_by_id(email)
passwd = driver.find_element_by_id(password)
uName.send_keys('kannan.wizkid@gmail.com')
passwd.send_keys('happy')
time.sleep(2)
driver.find_element_by_id(login).click()

#delay 5 seconds
time.sleep(5)

#crawl followers
useridList = {}
userid=[]
#node_count=0
def crawl(nextuser):
	userid = []
	if nextuser not in useridList:
		global node_count
		nextuserurl = "http://www.quora.com/"+nextuser+"/followers"
		driver.get(nextuserurl)
		for x in range(0,15):
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(0.5)
		source = driver.page_source
		soup = BeautifulSoup(source.encode('utf-8','ignore'))
		for temp in soup.findAll('a',class_='user'):
			var = temp.get('href')
			var1=var.split('/')[1]
			var2=var1.split('?')[0]
			#if var2 not in userid:
			userid.append(var2)
		userid = list(set(userid))
		useridList[nextuser]=userid
		#node_count+=1
		print 'node: ', len(useridList) , 'username: ' , nextuser , 'followers: ', len(userid)

#starting user link
ubername = 'Harini-Ravichandran'
crawl(ubername)

while len(useridList)<50:
	for key in useridList.keys():
		 
		for x in useridList[key]:
			if len(useridList)<50:
				time.sleep(0.05)
				crawl(x)
#writing to CSV file
writer = csv.writer(open('out.csv', 'wb'))
for key, value in useridList.items():
	writer.writerow([key,value])