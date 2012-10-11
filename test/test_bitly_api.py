#!/usr/local/bin/python
"""
This is a py.test script
"""
import datetime
import sys
sys.path.append('../')
import bitly_api

def testApi():
    bitly = bitly_api.Connection('bitlyapidemo','R_0da49e0a9118ff35f52f629d2d71bf07')
    data = bitly.shorten('http://google.com/')
    assert data != None
    assert data['long_url'] == 'http://google.com/'
    assert data['hash'] != None
    
def testExpand():
    bitly = bitly_api.Connection('bitlyapidemo','R_0da49e0a9118ff35f52f629d2d71bf07')
    data = bitly.expand(hash='test1')
    assert data != None
    assert len(data) == 1
    assert data[0]['error'] == 'NOT_FOUND'
    
def testReferrer():
    bitly = bitly_api.Connection('bitlyapidemo','R_0da49e0a9118ff35f52f629d2d71bf07')
    data = bitly.referrers(hash='a')
    assert data != None
    assert len(data) > 1

def testProDomain():
    bitly = bitly_api.Connection('bitlyapidemo','R_0da49e0a9118ff35f52f629d2d71bf07')
    test_data = {
        'cnn.com': False,
        'nyti.ms': True,
        'g.co': False,
        'j.mp': False,
        'pep.si': True,
        'http://pep.si': 'INVALID_BARE_DOMAIN',
    }
    for domain in test_data:
        try:
            result = bitly.pro_domain(domain)
            assert result == test_data[domain], domain
        except bitly_api.BitlyError, e:
            assert str(e) == test_data[domain]

# Bundle tests

def testBundleCreate():
    bitly = bitly_api.Connection('bitlyapidemo','R_0da49e0a9118ff35f52f629d2d71bf07')
    title = "Test Bundle  " + datetime.datetime.today().strftime("%Y%m%d%H%M%S")
    description = "Testing API"
    access_token = "insert access token here"
    private = False
    data = bitly.bundle_create(title, description, private, access_token)
    assert data != None

def testBundleAddLink():
    bitly = bitly_api.Connection('bitlyapidemo','R_0da49e0a9118ff35f52f629d2d71bf07')
    bundle_url = "http://bitly.com/bundles/bitlyapidemo/1"
    url_to_add = "http://google.com/"
    access_token = "insert access token here"
    data = bitly.bundle_add_link(bundle_url, url_to_add, access_token)
    assert data != None
