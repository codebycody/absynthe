def request_verb_tests(data):
    verb = data.split(' ',1)[0]
    print(verb)
    match verb.upper():
        case 'POST':
            print('found a post')
            # injection attack
            # cross site scripting
            # CSRF
            # Broken Authentication and session management
            # Insecure Deserialization
            # Security Misconfiguration
            # File Upload vuln
        case 'GET':
            print('found a get')
            # caching issues
            # unvalidated redirects
            # Inadwqute authorization
            # IDOR
            # Sensitive Data Exposure
            # CSRF
            # XSS
            # Injection Attacks
        case 'PUT':
            print('found a put')
            # injection attack
            # Sensitive Data Exposure
            # Broken Authentication
            # IDOR
            # HTTP verb Testing_for_HTTP_Verb_Tampering
        case 'PATCH':
            print('found a patch')
            # Poor Validation
            # Sensitive Data Exposure
            # Broken Authentication and Session Management
            # Security Misconfiguration
            # Insecure Direct Object References
            # Missing or Inadequate Authorization
            # Business Logic Vulnerabilities
            # Input Validation and Data Sanitization
            # HTTP Verb Tampering
            # Denail of Service
        case 'DELETE':
            print('found a delete')
            # Missing or Inadequate Authorization
            # Insecure Direct Ibject References
            # Broken Authentication and Session MAnagement
            # Security Misconfiguration
            # Business Logic Vulnerabilities
            # Denial of Service
            # Sensitvie Data Exposure
            # HTTP Verb Tampering
            # HTTP Verb Spoofing
        case 'OPTIONS':
            print('found a options')
            # Information Disclosure
            # CORS Misconfiguration
            # HTTP Verb Tampering
            # Security Headers
            # Insecure Methods and Headers
        case 'HEAD':
            print('found a head')
            # Caching Headers
            # HTTP Verb Tampering
        case 'CONNECT':
            print('found a connect')
        case 'TRACE':
            print('found a trace')

def request_header_tests(data):
	header = data
	print(header)

