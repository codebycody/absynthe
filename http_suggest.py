import sys
import re
import requests
from http_tests import *

def request_verb_test(request_data):
    request_verb_test = request_data.split('\n',1)[0]
    request_verb_tests(request_verb_test)
    return request_verb_test

def status_test(response_data):
    response_status = response_data.split('\n',1)[0]
    return response_status

def header_test(http_data):
    headers_pattern = r"(.*?: .*?)(?:\n|$)"
    results = re.findall(headers_pattern, http_data)
    request_header_tests(request_verb_test)
    return results

def body_test(http_data):
    try:
        results = http_data.split('\n\n', 1)[1]
    except:
        results = ''
    return results

def parse_request_response(request_data, response_data):
    # Parse request data
    request_parts = request_data.split('\n\n', 1)
    request_line = request_verb_test(request_data)
    request_headers = header_test(request_data)
    request_body = body_test(request_data)

    # Parse response data
    response_parts = response_data.split('\n\n', 1)
    response_status = status_test(response_data)
    response_headers = header_test(response_data)
    response_body = body_test(response_data)


    return {
        "Request Line": request_line,
        "Request Headers": request_headers,
        "Request Body": request_body,
        "Response Status": response_status,
        "Response Headers": response_headers,
        "Response Body": response_body
    }

def save_output(output_data):
    with open("output.txt", "w") as file:
        for section, content in output_data.items():
            file.write(f"=== {section} ===\n{content}\n\n")

if len(sys.argv) != 3:
    print("Usage: python script.py <request_data> <response_data>")
else:
    request_data = sys.argv[1]
    response_data = sys.argv[2]

    parsed_data = parse_request_response(request_data, response_data)
    save_output(parsed_data)
    # print("Output saved to 'output.txt'")
