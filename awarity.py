#!/usr/bin/python

import secrets
import mechanize
from linkedin import linkedin
import time
import random

def authenticate():
        authentication = linkedin.LinkedInDeveloperAuthentication(secrets.API_KEY, \
                                                                  secrets.API_SECRET, \
                                                                  secrets.USER_TOKEN, \
                                                                  secrets.USER_SECRET, \
                                                                  secrets.RETURN_URL, \
                                                                  linkedin.PERMISSIONS.enums.values())
        application = linkedin.LinkedInApplication(authentication)
        return application

def startLinkedInBrowser():
        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        browser.open("https://www.linkedin.com/")
        browser.select_form(name="login")

        browser["session_key"] = secrets.LINKEDIN_USERNAME
        browser["session_password"] = secrets.LINKEDIN_PASSWORD
        response = browser.submit()
        return browser

"""
authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())

AUTH_ONLY=False

if (AUTH_ONLY):
    print authentication.permissions
    print authentication.authorization_url  
    raw_input("Open this link in browser...");
    quit();

CODE = 'AQRnjvb4w8ze1T6C31hM9dEBCQIqMA3AnLP6v_9TwwAY0LkAyLmAakglWJOJA2n7KAFl1n7RUrGOJJDwHcg8tjSMsxXNim5PkyzjdMwhem8SOAAJLBg&state=ffbef8dbec56a2bd37bcc88e0b931b2d'

authentication.authorization_code = CODE;
access_token = authentication.get_access_token();
"""

#print application.get_profile()
#print application.get_connections()
#print application.search_profile(selectors=[{'people':['first-name', 'last-name']}],params={'keywords':'nolan van heerden'})

application = authenticate()
connections = application.get_connections()
browser = startLinkedInBrowser()

for connection in connections[u'values']:
        try:
                print ">>" + connection[u'firstName'] + " " + connection[u'lastName'] + " " + connection[u'id'] + "\n" + connection[u'siteStandardProfileRequest'][u'url']
                URL = connection[u'siteStandardProfileRequest'][u'url']
                # - do not overburder people with views!! 
                #browser.open(URL)
        except:
                print '=== No Standard Profile ==='
                print connection.keys()

        #random time delay
        time.sleep(random.randint(10,100))

