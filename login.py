from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import csv

#retrieving source file
driver = webdriver.Chrome()
driver.get('http://www.quora.com')
source = driver.page_source
soup = BeautifulSoup(source)

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
driver.find_element_by_id(login).click()

#delay 5 seconds
time.sleep(5)

#source followers page
homeprof = "https://www.quora.com/Kannan-Ravindran/followers"
driver.get(homeprof)

#crawl followers
scrl_count=0
usr_count=0
node_count=0
for x in range(0,500):
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	scrl_count+=1
source = driver.page_source
soup = BeautifulSoup(source)
useridList = {}
userid=[]
for temp in soup.findAll('a',class_='user'):
	var = temp.get('href')
	usr_count+=1
	var1=var.split('/')[1]
	var2=var1.split('?')[0]
	if var2 not in userid:
		userid.append(var2)
useridList['me']=userid
node_count+=1
print 'User: Kannan-Ravindran ','Node: ',node_count, 'Followers: ',usr_count

#subsequent users
for x in range (0,10):
	temp_usr=usr_count
	nextuser = userid[x]
	nextuserurl = "https://www.quora.com/"+nextuser+"/followers"
	driver.get(nextuserurl)
	for x in range(0,500):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		scrl_count+=1
	source = driver.page_source
	soup = BeautifulSoup(source)
	for temp in soup.findAll('a',class_='user'):
		var = temp.get('href')
		usr_count+=1
		var1=var.split('/')[1]
		var2=var1.split('?')[0]
		if var2 not in userid:
			userid.append(var2)
	print userid
	useridList[nextuser]=userid
	node_count+=1
	print 'User: ',nextuser,'Node: ',node_count, 'Followers: ',usr_count-temp_usr


#print the userlist
'''for y in useridList:
	print useridList[y]
'''#print useridList
print '\n'
print 'scrolls: ',scrl_count
print 'users crawled: ',usr_count

#writing to CSV file
f = open("users.csv", "wb")
w = csv.writer(f)
for key, val in useridList.items():
	w.writerow([key,val])
f.close()