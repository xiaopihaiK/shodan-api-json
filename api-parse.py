import json

# mongoimport.exe --db shodan_data --collection phpmyadmin_data --file E:\share\shodan-export.json\shodan_data.json


f = open('web.json','r')

s = json.loads(f.read())

############Get shodan api json number of key ################################
for i in range(0,100):
	for x in s["matches"][i]:
		if len(x)==9:
			print i
############Get shodan api json every key value###############################
for i in range(0,100):
	print s["matches"][i]
############Get shodan api json every key to value############################
for i in range(0,100):
	print 'key: '+str(i)+' ---- '+str(s["matches"][i])
###############################################################################
