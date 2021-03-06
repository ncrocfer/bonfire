'''
Created on 20.04.15

@author = mharder
'''

from __future__ import division, print_function

from bonfire.utils import api_from_config, api_from_host

def test_api_from_host():
    host = "test_host"
    port = 1235
    user = "test"
    api = api_from_host(host, port, user)

    assert api.host == host
    assert api.port == port
    assert api.username == user