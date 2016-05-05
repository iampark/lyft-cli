lyft-cli
===

Simple implementation of a CLI against the Lyft API that implements OAuth2 and allows for URL-based calls.

To run this sample code, you'll need to install the following python libraries:

- Sanction, modified: [https://github.com/iampark/sanction](https://github.com/iampark/sanction)

This modified version has a workaround to support the Basic Auth headers that Lyft requires during the OAuth process.

You can install the above by running:

    pip install -r requirements.txt

Getting Started
---
Create a [Lyft App](https://developer.lyft.com/).

Specify your Lyft App keys and tokens in a new config file named .lyft. There is a sample config file named .lyft.sample:

Run the python script in the project directory:

```
python Lyft.py
```

Requests
---

### Public

The below methods are documented at [https://developer.lyft.com/docs](https://developer.lyft.com/docs).

> GET /eta?lat=47.587681&lng=-120.393384&ride_type=lyft

> GET /rides?start_time=2015-01-01T00%3A00%3A00%2B00%3A00

### Private

The below methods are what the Lyft app uses, and can be seen using [this technique](https://www.moncefbelyamani.com/how-to-capture-iphone-and-ipad-network-traffic-with-charles/).

> PUT https://api.lyft.com/users/222669192517078410/location

    {"marker":{"lat":47.58755990190871,"lng":-120.3912808076761},"appInfoRevision":"","locations":[{"speed":-1,"lng":-120.3912808076761,"fg":false,"recordedAt":"2016-05-03T07:06:07Z","lat":47.58755990190871,"accuracy":65,"userMode":"passenger"}]}

Response can be found in the `user.json` file

> GET /notifications?screenWidth=475&screenHeight=667

> GET /venues?lat=47.58754000929794&lng=-120.391293869279 HTTP/1.1


Issues
-----

- Not having a `user` endpoint means its difficult (impossible?) to integrate into standard OAuth libraries (python-social-auth)
- Reliance on Basic Auth `client:secret` header isn't standard for OAuth2, is it?
- 3-legged auth: state is required, even if it's not useful/dummy param. Otherwise OAuth fails.
- Swagger support to auto-generate stubs for Lyft API in Python is poor, because:
    - YAML support is scarse (JSON format more readily supported)
    - YAML support over HTTP was even more scare (couldn't find a library that did it)
    - Support for OAuth2 with "Basic Auth" step is unsupported/uncommon
- swagger.io site (linked to from docs) doesn't successfully auth and/or make requests
- For basic samples, need .bashrc to have:

    export PYTHONPATH=$PYTHONPATH:/Library/Python/2.7/site-packages
