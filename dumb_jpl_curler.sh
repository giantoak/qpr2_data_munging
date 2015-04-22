#!/bin/bash
curl "http://memex.dyndns.org:8081/solr/imagecatdev/select?q=*%3A*&wt=json&rows=5000&page=[1-100000:5000]"
