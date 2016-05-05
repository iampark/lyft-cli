import json
import urllib
import ConfigParser

from sanction import Client, transport_headers

config = ConfigParser.ConfigParser()
config.read('.lyft')

client_id = config.get('lyft', 'client')
client_secret = config.get('lyft', 'secret')

auth_endpoint = 'https://api.lyft.com/oauth/authorize'
token_endpoint = 'https://api.lyft.com/oauth/token'
resource_endpoint = "https://api.lyft.com/v1"

prompt = '\nEnter a URI (Q to quit):\n> '

data = {"lat": 37.587681, "lng": -122.393384, "ride_type": "lyft"}
data = urllib.urlencode(data)
example_url_eta = "/eta?%s" % data

data = {"start_time": "2015-01-01T00:00:00+00:00"}
data = urllib.urlencode(data)
example_url_rides = "/rides?%s" % data


def pretty(js):
    print json.dumps(js, sort_keys=True, indent=4, separators=(',', ': '))

def main():

    # instantiating a client to process OAuth2 response
    c = Client(
        auth_endpoint=auth_endpoint,
        token_endpoint=token_endpoint,
        resource_endpoint=resource_endpoint,
        client_id=client_id,
        client_secret=client_secret,
        token_transport=transport_headers)

    # 3-legged (read/write)
    scope_req = 'public rides.read rides.request'
    url = c.auth_uri(scope=scope_req, scope_delim=' ', state='asdf')

    print "Welcome to the API client tool for"
    print ""
    print "    IIIII7MMMMMMMMMMMMMMMMMMM7IIIIIII7MMMMMM"
    print "    IIIII7MMMMMMMMMMMMMMMMMIIIIIIIIIIII7MMMM"
    print "    IIIII7MMMMMMMMMMMMMMMMIIIIIIIIIIIIIIIMMM"
    print "    IIIII7MMMMMMMMMMMMMMMMIIIIII7M7IIIIIIMMM"
    print "    IIIII7MIIIIIIMNIIIIIZDIIIIINMMMZIIIIIIIM"
    print "    IIIII7MIIIIIIMNIIIIIZ8IIIIIMMMM8IIIIIIIM"
    print "    IIIII7MIIIIIIMNIIIIIZ8IIIIIIIIN8IIIIIIIM"
    print "    IIIII7MIIIIIIMNIIIIIZ8IIIIIIIIN8IIIIIMMM"
    print "    IIIII7MIIIIIIMNIIIIIZ8IIIIIIIIN8IIIIIMMM"
    print "    IIIII7MIIIIIIMIIIIIIZ8IIIII777NMIIIII7MM"
    print "    IIIII7MIIIIIIIIIIIIIZ8IIIIIMMMMMIIIIIIID"
    print "    IIIIIIMIIIIIIIIIIIIIZ8IIIIIMMMMMMIIIIIID"
    print "    MIIIII7MIIIIIIIIIIIIO8III7MMMMMMMMMIIIID"
    print "    MMD7IIIMMMMMMMIIIIIIMD78MMMMMMMMMMMMMMOD"
    print "    MMMMMMMMNIIIIIIIIIIIMMMMMMMMMMMMMMMMMMMM"
    print "    MMMMMMMMNIIIIIIIIIIMMMMMMMMMMMMMMMMMMMMM"
    print "    MMMMMMMMNIIIIIIII7MMMMMMMMMMMMMMMMMMMMMM"
    print "    MMMMMMMMMMMZ78MMMMMMMMMMMMMMMMMMMMMMMMMM"
    print ""
    print "STEP 1: Authenticate a user by opening this URL in a browser (Command + Double Click):\n\n%s" % url
    print ""
    code = raw_input("STEP 2: After authenticating, paste the 'code' parameter in the redirect URL here: ")

    result = c.request_token(grant_type='authorization_code', code=code)

    print "\nSTEP 3: There is no Step 3. You are now authenticated to the Lyft API. Congratulations!"

    print "\nEnter a URI to start testing. Some examples:\n\n\t%s --> ETA for location\n\t%s --> Rides for location" % (example_url_eta, example_url_rides)

    command = raw_input(prompt)

    while command != 'Q':

        try:

            method = "GET"
            data = None

            if " " in command:
                (method, command, data) = command.split(" ")

            result = c.request(command, method=method, data=data)
            pretty(result)

        except Exception as ex:

            import traceback
            traceback.print_exc()

        command = raw_input(prompt)

if __name__ == "__main__":
    main()


