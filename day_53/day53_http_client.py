

import http.client

connection = http.client.HTTPSConnection('127.0.0.1', 8080, timeout=10)
print(connection)
connection.request("GET", "/")
response = connection.getresponse()
print("Status: {} and reason: {}".format(response.status, response.reason))

connection.close()