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

#print application.search_profile(selectors=[{'people':['first-name', 'last-name']}],params={'keywords':'nolan van heerden'})

def iterateThroughConnections():
        application = authenticate()
        connections = application.get_connections()
        browser = startLinkedInBrowser()

        for connection in connections[u'values']:
                try:
                        print ">>" + connection[u'firstName'] + \
                              " " + connection[u'lastName'] + \
                              " " + connection[u'id'] + "\n" + \
                              connection[u'siteStandardProfileRequest'][u'url']

                        URL = connection[u'siteStandardProfileRequest'][u'url']

                        # - do not overburder people with views!! 
                        #browser.open(URL)
                except:
                        print '=== No Standard Profile ==='
                        print connection.keys()

                #random time delay
                time.sleep(random.randint(10,100))

def showConnectionStats(connections):
        print "Total Number of Connections: " + str(connections[u'_total'])
        rand = random.randint(0, connections[u'_total']-1)
        print "Random Connection Names: " + connections[u'values'][rand][u'firstName'] + " " + \
                                           connections[u'values'][rand][u'lastName']

def main():
        print '[Authenticating application]'
        application = authenticate()

        print '[Retrieve connections]'
        connections = application.get_connections()

        print '[Show statistics - demo use]'
        showConnectionStats(connections);

if __name__ == "__main__":
        main()
