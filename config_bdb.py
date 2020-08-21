import json

# read the file
with open('.bigchaindb','r') as file:
    data = file.read().replace('\n','')
    file.close()
data = json.loads(data)
# Change server bind
data['server']['bind'] = "0.0.0.0:9984"
data = json.dumps(data,indent=4,sort_keys=False)
with open('.bigchaindb','w') as file:
    file.write(data)
    file.close()

