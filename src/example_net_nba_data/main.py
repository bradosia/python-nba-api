import http.client
import json

# compare two proteins
def main():
        conn = http.client.HTTPSConnection("data.nba.net")
        conn.request("GET", "/")
        r1 = conn.getresponse()
        # print(r1.status, r1.reason)
        data1 = r1.read()  # This will return entire content.
        # The following example demonstrates reading data in chunks.
        conn.request("GET", "/")
        r1 = conn.getresponse()
        httpGetJson = ''
        while chunk := r1.read(200):
                httpGetJson += chunk.decode("utf-8")
        # print (httpGetJson)
                
        # parse into JSON:
        parsed = json.loads(httpGetJson)

        # print JSON
        print(json.dumps(parsed, indent=2, sort_keys=True))

if __name__ == '__main__':
	main()
