import urllib2
import json

url ="http://10.15.21.11:8080/api/v1/namespaces/default/replicationcontrollers/tensorflow-worker0-rc"

result = urllib2.urlopen(url).read()
rc = json.loads(result)
#change this replicas
rc["spec"]["replicas"] = 1

opener = urllib2.build_opener(urllib2.HTTPHandler)
request = urllib2.Request(url, data=json.dumps(rc, sort_keys=True, indent=4))
request.add_header("Content-Type", "application/json")
request.get_method = lambda:"PUT"
rr = opener.open(request)
