import json
from urlparse import urlparse
import httplib2 as http
import datetime
import sys
from elasticsearch import Elasticsearch


if __name__=="__main__":
 pwd = "/home/cjaiwenwen/PycharmProjects/chenjun/LTA"
 ES_CLUSTER = "http://localhost:9200"
 ES_INDEX= 'LTA'
 ES_TYPE = "doc"
 es = Elasticsearch(ES_CLUSTER)
 #Authentication parameters
 headers = { 'AccountKey' : 'KEY',
             'UniqueUserID' : 'ID',
             'accept' : 'application/json'} #Request results in JSON

 #API parameters
 uri = 'http://datamall2.mytransport.sg/' #Resource URL
 path = '/ltaodataservice/TrafficIncidents?'
 path1 = '/ltaodataservice/BusStops?$skip=1100'
 path2 = '/ltaodataservice/CarParkAvailability?$skip=200?'

 #Build query string & specify type of API call
 target = urlparse(uri + path)
 print target.geturl()
 method = 'GET'
 body = ''

 #Get handle to http
 h = http.Http()
 #Obtain results
 response, content = h.request(
               target.geturl(),
               method,
               body,
               headers)
 #Parse JSON to print
 jsonObj = json.loads(content)
 filename = datetime.date.today()
 with open ("%s/%s.json"%(pwd,filename), "w+") as f:
     sys.stdout = f
     print json.dumps(jsonObj, sort_keys=True, indent=4)

 f.close()


