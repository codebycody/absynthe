from bs4 import BeautifulSoup
import urllib.request


def fileImported():
    return "fileImported correctly"

def spiderAsset():
    # Need to get urls from the main target
    ##########################################
    # Add main url to check list
    # Check for a sitemap.xml add to check list
    # go threw each on check list looking for internal urls add them to the check list
    # keep track of urls marketed in the already crawled section
    return True

def headersCheck(target):
    # getting a 403 forbidden response for this test need to find a way to check headers
    source = urllib.request.urlopen("https://securityheaders.com/?q=" + target + "&followRedirects=on").read()
    soup = BeautifulSoup(source, 'html.parser')
    return soup

def openRedirect():
    # check for open redirect issues
    return findings

def httpParameterPollution():
    # check for HTTP Parameter Pollution
    return findings

def csrf():
    # check for CROSS-SITE Request Forgery
    return findings

def contentSpoofing():
    # check for html injection and content spoofing
    return findings

def xss():
    # check for Cross Site Scripting
    return findings

def templateInjection():
    # check for template injections
    return findings

def sqlInjection():
    # check for sql injections
    return findings

def serversideRequestForgery():
    # check for server side request forgery
    return findings

def xmlExternalEntity():
    # check for xml external entity
    return findings

def remoteCodeExecution():
    # check for rce vulnerability
    return findings

def memoryVulnerabilities():
    # check for memory vulnerabilities
    return findings

def subdomainTakeOver():
    # check for subdomain take over
    return findings

def raceConditions():
    # check for race conditions
    return findings

def idcr():
    # check for insecure direct object reference
    return findings

def oauthVulns():
    # check for oauth vulnerabilities
    return findings

def configuration():
    # check for configuaration vulnerabilites
    return findings

