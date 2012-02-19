# Create your views here.
from django.core import serializers
import urllib2
import json

site_url='http://intranet.festival-salon.fr/api/artists/'


def load_json(url):
	req = urllib2.Request(url)
	r = urllib2.urlopen(req)
	d = r.read()
	j = json.loads(d)
	datas = serializers.deserialize('json',j)

