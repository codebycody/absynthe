import requests

# What is information disclosure?
### Information disclosure, also known as information leakage, is when a website unintentionally reveals sensitive information to its users. Depending on the context, websites may leak all kinds of information to a potential attacker, including:
###   Data about other users, such as usernames or financial information
###   Sensitive commercial or business data
###   Technical details about the website and its infrastructure
### The dangers of leaking sensitive user or business data are fairly obvious, but disclosing technical information can sometimes be just as serious. Although some of this information will be of limited use, it can potentially be a starting point for exposing an additional attack surface, which may contain other interesting vulnerabilities. The knowledge that you are able to gather could even provide the missing piece of the puzzle when trying to construct complex, high-severity attacks.
### Occasionally, sensitive information might be carelessly leaked to users who are simply browsing the website in a normal fashion. More commonly, however, an attacker needs to elicit the information disclosure by interacting with the website in unexpected or malicious ways. They will then carefully study the website's responses to try and identify interesting behavior.
# Common sources of information disclosure
## Files for web crawlers file_for_web_crawlers()
### As these files are not usually linked from within the website, they may not immediately appear in Burp's site map. However, it is worth trying to navigate to /robots.txt or /sitemap.xml manually to see if you find anything of use.
### Many websites provide files at /robots.txt and /sitemap.xml to help crawlers navigate their site. Among other things, these files often list specific directories that the crawlers should skip, for example, because they may contain sensitive information.
## Directory listings directory_listings()
###  Web servers can be configured to automatically list the contents of directories that do not have an index page present. This can aid an attacker by enabling them to quickly identify the resources at a given path, and proceed directly to analyzing and attacking those resources. It particularly increases the exposure of sensitive files within the directory that are not intended to be accessible to users, such as temporary files and crash dumps.
### Directory listings themselves are not necessarily a security vulnerability. However, if the website also fails to implement proper access control, leaking the existence and location of sensitive resources in this way is clearly an issue.
## Developer comments developer_comments()
### During development, in-line HTML comments are sometimes added to the markup. These comments are typically stripped before changes are deployed to the production environment. However, comments can sometimes be forgotten, missed, or even left in deliberately because someone wasn't fully aware of the security implications. Although these comments are not visible on the rendered page, they can easily be accessed using Burp, or even the browser's built-in developer tools.
### Occasionally, these comments contain information that is useful to an attacker. For example, they might hint at the existence of hidden directories or provide clues about the application logic.
## Error messages error_messages()
###  One of the most common causes of information disclosure is verbose error messages. As a general rule, you should pay close attention to all error messages you encounter during auditing.
### The content of error messages can reveal information about what input or data type is expected from a given parameter. This can help you to narrow down your attack by identifying exploitable parameters. It may even just prevent you from wasting time trying to inject payloads that simply won't work.
### Verbose error messages can also provide information about different technologies being used by the website. For example, they might explicitly name a template engine, database type, or server that the website is using, along with its version number. This information can be useful because you can easily search for any documented exploits that may exist for this version. Similarly, you can check whether there are any common configuration errors or dangerous default settings that you may be able to exploit. Some of these may be highlighted in the official documentation.
## Debugging data debugging_data()
### For debugging purposes, many websites generate custom error messages and logs that contain large amounts of information about the application's behavior. While this information is useful during development, it is also extremely useful to an attacker if it is leaked in the production environment.
### Debug messages can sometimes contain vital information for developing an attack, including:
###    Values for key session variables that can be manipulated via user input
###    Hostnames and credentials for back-end components
###    File and directory names on the server
###    Keys used to encrypt data transmitted via the client
### Debugging information may sometimes be logged in a separate file. If an attacker is able to gain access to this file, it can serve as a useful reference for understanding the application's runtime state. It can also provide several clues as to how they can supply crafted input to manipulate the application state and control the information received.
## User account pages user_account_pages()
### By their very nature, a user's profile or account page usually contains sensitive information, such as the user's email address, phone number, API key, and so on. As users normally only have access to their own account page, this does not represent a vulnerability in itself. However, some websites contain logic flaws that potentially allow an attacker to leverage these pages in order to view other users' data.
### For example, consider a website that determines which user's account page to load based on a user parameter.
###    GET /user/personal-info?user=carlos
### Most websites will take steps to prevent an attacker from simply changing this parameter to access arbitrary users' account pages. However, sometimes the logic for loading individual items of data is not as robust.
### An attacker may not be able to load another users' account page entirely, but the logic for fetching and rendering the user's registered email address, for example, might not check that the user parameter matches the user that is currently logged in. In this case, simply changing the user parameter would allow an attacker to display arbitrary users' email addresses on their own account page.
## Source code disclosure via backup files source_code_disclosure_via_backup_files()
### Obtaining source code access makes it much easier for an attacker to understand the application's behavior and construct high-severity attacks. Sensitive data is sometimes even hard-coded within the source code. Typical examples of this include API keys and credentials for accessing back-end components.
### If you can identify that a particular open-source technology is being used, this provides easy access to a limited amount of source code.
### Occasionally, it is even possible to cause the website to expose its own source code. When mapping out a website, you might find that some source code files are referenced explicitly. Unfortunately, requesting them does not usually reveal the code itself. When a server handles files with a particular extension, such as .php, it will typically execute the code, rather than simply sending it to the client as text. However, in some situations, you can trick a website into returning the contents of the file instead. For example, text editors often generate temporary backup files while the original file is being edited. These temporary files are usually indicated in some way, such as by appending a tilde (~) to the filename or adding a different file extension. Requesting a code file using a backup file extension can sometimes allow you to read the contents of the file in the response.
## Information disclosure due to insecure configuration information_disclosure_due_to_insecure_configuration()
### Websites are sometimes vulnerable as a result of improper configuration. This is especially common due to the widespread use of third-party technologies, whose vast array of configuration options are not necessarily well-understood by those implementing them.
### In other cases, developers might forget to disable various debugging options in the production environment. For example, the HTTP TRACE method is designed for diagnostic purposes. If enabled, the web server will respond to requests that use the TRACE method by echoing in the response the exact request that was received. This behavior is often harmless, but occasionally leads to information disclosure, such as the name of internal authentication headers that may be appended to requests by reverse proxies.
## Version control history version_control_history()
### Virtually all websites are developed using some form of version control system, such as Git. By default, a Git project stores all of its version control data in a folder called .git. Occasionally, websites expose this directory in the production environment. In this case, you might be able to access it by simply browsing to /.git.
### While it is often impractical to manually browse the raw file structure and contents, there are various methods for downloading the entire .git directory. You can then open it using your local installation of Git to gain access to the website's version control history. This may include logs containing committed changes and other interesting information.
### This might not give you access to the full source code, but comparing the diff will allow you to read small snippets of code. As with any source code, you might also find sensitive data hard-coded within some of the changed lines.

def file_for_web_crawlers(hostname):
    ## TODO: {get the response, parse to see if data is the expected, add way of grouping findings, return the findings in a key value pair}
    #robots.txt
    robots = requests.get('http://' + hostname + '/robots.txt')
    #sitemap.xml
    sitemap = requests.get('http://' + hostname + '/sitemap.xml')

def directory_listings(hostname):
    ## TODO: {make request to page, identify if the page is a default directory listing page, save paths for discovered paths, return findings in a key value pair}
    return True

def developer_comments(path):
    ## TODO: {parse through path|input for comment tags, store found comments, return found comments in a key value pair}
    return True

def error_messages(content):
    ## TODO: {parse through content for error data, store found instants of data, return found error data in a key value pair}
    return True

def debugging_data(content):
    ## TODO: {parsse through content for debugging data, store found instanties of data, return found data in a key value pair}
    return True

def user_account_pages(host):
    ## TODO: {get list of default user page paths e.g. (https://wordpressexample.com/wp-json/wp/v2/users), store findings, return data in a key value pair}
    return True

def source_code_disclosure_via_backup_files(host):
    ## TODO: {get list of default backup file paths, store findings, return data in a key value pair}
    return True

def information_disclosure_due_to_insecure_configuration(host):
    ## TODO: {get list of tests to run, store findings, return data in a key value pair}
    return True

def version_control_history(host):
    ## TODO: {get list of version control default paths, store findings, return data in a key value pair}
    return True

def main(target):
    file_for_web_crawlers(target)

if __name__ == '__main__':
    main('demo.firetest.net')
