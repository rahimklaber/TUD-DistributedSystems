# testcase 2: Add v1 on any node, add arc (v1, v2), lookup arc (v1, v2)(exp. false), Add v2, lookup arc (v1, v2)
# expected false, true

import requests

vertex1 = {"vertexName": "v1"}
vertex2 = {"vertexName": "v2"}

arcv1_v2 = {"sourceVertex": "v1", "targetVertex": "v2"}
arcv2_v1 = {"sourceVertex": "v2", "targetVertex": "v1"}

url = "http://localhost:"
node1_port = "7000"
node2_port = "7001"
node3_port = "7002"
addvertex_endpoint = "/addvertex"
addarc_endpoint = "/addarc"
lookupvertex_endpoint = "/lookupvertex"
removevertex_endpoint = "/removevertex"
removearc_endpoint = "/removearc"
lookuparc_endpoint = "/lookuparc"

print("Adding vertex " + vertex1['vertexName'] + " on node with port " + node1_port)
r1 = requests.post(url + node1_port + addvertex_endpoint, json=vertex1)
print(r1.text)

print("adding arc between v1 and v2 on node with port " + node1_port)
r1 = requests.post(url + node1_port + addarc_endpoint, json=arcv1_v2)
print(r1.text)


print("looking up newly created arc")
r1 = requests.get(url + node1_port + lookuparc_endpoint + "?sourceVertex=v1&targetVertex=v2")
print(r1.text)

print("Adding vertex " + vertex2['vertexName'] + " on node with port " + node1_port)
r1 = requests.post(url + node1_port + addvertex_endpoint, json=vertex2)
print(r1.text)

print("looking up newly created arc")
r1 = requests.get(url + node1_port + lookuparc_endpoint + "?sourceVertex=v1&targetVertex=v2")
print(r1.text)