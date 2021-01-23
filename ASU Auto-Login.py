#pip install selenium if you don't have it installed
from selenium import webdriver

#I make a webdriver for Firefox
driver = webdriver.Firefox()

#open up myASU.com
driver.get("https://weblogin.asu.edu/cas/login?service=https%3A%2F%2Fweblogin.asu.edu%2Fcgi-bin%2Fcas-login%3Fcallapp%3Dhttps%253A%252F%252Fwebapp4.asu.edu%252Fmyasu%252F%253Finit%253Dfalse")

#look for the username field
username = driver.find_element_by_xpath('//*[@id="username"]')
#type in your username
username.send_keys("Put in your usersname")


#look for the password field
password = driver.find_element_by_xpath('//*[@id="password"]')
#type in your password
password.send_keys("Put in your password")

#click on next button
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div/div/form/section[2]/div[1]/input').click()


