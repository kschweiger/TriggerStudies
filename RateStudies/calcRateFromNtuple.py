import ROOT
import countEvents
from math import sqrt
#################################
# User input
basepath = "/mnt/t3nfs01/data01/shome/koschwei/scratch/HLT2018Tuning/RateEstimation/RunF/"
inputfiles = ["EphemeralHLTPhysics1/EphemeralHLTPhysics1.root",
              "EphemeralHLTPhysics2/EphemeralHLTPhysics2.root",
              "EphemeralHLTPhysics3/EphemeralHLTPhysics3.root",
              "EphemeralHLTPhysics4/EphemeralHLTPhysics4.root",
              "EphemeralHLTPhysics5/EphemeralHLTPhysics5.root",
              "EphemeralHLTPhysics6/EphemeralHLTPhysics6.root",
              "EphemeralHLTPhysics7/EphemeralHLTPhysics7.root",
]
              
nLS = 248
PS = 1160
avLumi = 344.3525 / nLS
lumiSF = 1
#################################

ROOT.TH1.SetDefaultSumw2(True)
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

print avLumi

TLS = 23.31 #seconds

results = {}

nPasseds = {}
nPassedsErr = {}
rates = {}
ratesErr = {}
orderedpaths = []
nTot = 0
for ifile, _file in enumerate(inputfiles):
    print "---------------------------------------------"
    Rinput = ROOT.TFile.Open(basepath+_file)
    tree = Rinput.Get("tree")

    nTot += tree.Draw("","")
    print "Events in file {0}: {1}".format(_file, tree.Draw("",""))

    
    BranchesinFile = tree.GetListOfBranches()

    PathsinFile = []
    for b in BranchesinFile:
        if b.GetName().startswith("HLT_"):
            PathsinFile.append(b.GetName())
        if b.GetName().startswith("RAW_HLT_"):
            PathsinFile.append(b.GetName())
            
            

    for path in PathsinFile:

        nPassed = tree.Draw(path, "{0} == 1".format(path))
        nPassedErr = sqrt(nPassed)
        nFailed = tree.Draw(path, "{0} == 0".format(path))
        rate = lumiSF * PS * (float(nPassed) / (nLS *TLS) )
        rateErr = lumiSF * PS * (float(nPassedErr) / (nLS *TLS) )
        print "{0:>70} - {1:05.2f} +- {2:04.2f} - nPassed: {3:02}  +- {4:02.1f} - nFailed {5:06}".format(path, rate, rateErr, nPassed, nPassedErr, nFailed) 
        if ifile == 0:
            nPasseds[path] = [nPassed]
            nPassedsErr[path] = [nPassedErr]
            rates[path] = [rate]
            ratesErr[path] = [rateErr]
            orderedpaths.append(path)
        else:
            nPasseds[path].append(nPassed)
            nPassedsErr[path].append(nPassedErr)
            rates[path].append(rate)
            ratesErr[path].append(rateErr)

    pathpair = []
    for ipath,path in enumerate(PathsinFile):
        for path2 in PathsinFile:
            if path != path2 and (path[-10:] == path2[-10:]):
                pathpair.append((path, path2))
                PathsinFile.remove(path)


    for path1, path2 in pathpair:
        
        nPassed = tree.Draw("", "{0} == 1 || {1} == 1 ".format(path1, path2))
        nPassedErr = sqrt(nPassed)
        rate = lumiSF * PS * (float(nPassed) / (nLS *TLS) )
        rateErr = lumiSF * PS * (float(nPassedErr) / (nLS *TLS) )
        if ifile == 0:
            nPasseds[path1+"-"+path2] = [nPassed]
            nPassedsErr[path1+"-"+path2] = [nPassedErr]
            rates[path1+"-"+path2] = [rate]
            ratesErr[path1+"-"+path2] = [rateErr]
            orderedpaths.append(path1+"-"+path2)
        else:
            nPasseds[path1+"-"+path2].append(nPassed)
            nPassedsErr[path1+"-"+path2].append(nPassedErr)
            rates[path1+"-"+path2].append(rate)
            ratesErr[path1+"-"+path2].append(rateErr)
        #print "{0} or {1} {2}".format(path1, path2, rate)
print "---------------------------------------------"
print "---------------------------------------------"
print "---------------------------------------------"
print "Events over all Dataset: {0}".format(nTot)
for key in orderedpaths:
    mean = 0
    error = 0
    for ival, val in enumerate(rates[key]):
        mean += val
        error += ratesErr[key][ival]*ratesErr[key][ival]
    mean = mean/len(rates[key])
    error = (1.0/len(rates[key])) * sqrt(error)
    print "Path: {0:>70} -> Mean rate {1:05.2f} +- {2:04.2f}".format(key, mean, error)
