import json, yaml


#############################################
jsonFile = "nTuple/crab/json_DCSONLY.txt"
outfilenameprefix = "json_DCSONLY"
runToCount = "RunF"

#############################################

LSperRun = { "RunC" : (299337, 302029),
             "RunD" : (302030, 303434),
             "RunE" : (303435, 304826),
             "RunF" : (304911, 306462) }

validLS = None

with open(jsonFile, 'r') as f:
    validLS = yaml.safe_load(f) #json loads all entries as unicode (u'..')

RunLSs = {}
    
nLS = 0
for run in validLS:
    if int(run) >= LSperRun[runToCount][0] and int(run) < LSperRun[runToCount][1]:
        RunLSs[run] = validLS[run]
        for block in validLS[run]:
            #print block
            nLS += int(block[1]) - int(block[0]) + 1

with open(outfilenameprefix+"_"+runToCount+".json", "w") as outfile:
    json.dump(RunLSs, outfile, sort_keys=True,
              indent=4, separators=(',', ': '))

            
print "Number of LS in JSON: "+str(nLS)
