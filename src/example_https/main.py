'''
example from:
https://docs.python.org/3/library/http.client.html
'''

import http.client

# compare two proteins
def main():
        conn = http.client.HTTPSConnection("www.python.org")
        conn.request("GET", "/")
        r1 = conn.getresponse()
        print(r1.status, r1.reason)
        data1 = r1.read()  # This will return entire content.
        # The following example demonstrates reading data in chunks.
        conn.request("GET", "/")
        r1 = conn.getresponse()
        while chunk := r1.read(200):
                print(repr(chunk))

if __name__ == '__main__':
	main()
