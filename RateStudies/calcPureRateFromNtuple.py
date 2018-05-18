import ROOT
import countEvents
from math import sqrt
#################################
# User input
basepath = "/mnt/t3nfs01/data01/shome/koschwei/scratch/HLT2018Tuning/RateEstimation/RunF270218/FullMenu/"
inputfiles = [
    "EphemeralHLTPhysics1/EphemeralHLTPhysics1_mod.root",
    "EphemeralHLTPhysics2/EphemeralHLTPhysics2_mod.root",
    "EphemeralHLTPhysics3/EphemeralHLTPhysics3_mod.root",
    "EphemeralHLTPhysics4/EphemeralHLTPhysics4_mod.root",
    "EphemeralHLTPhysics5/EphemeralHLTPhysics5_mod.root",
    "EphemeralHLTPhysics6/EphemeralHLTPhysics6_mod.root",
    "EphemeralHLTPhysics7/EphemeralHLTPhysics7_mod.root",
    "EphemeralHLTPhysics8/EphemeralHLTPhysics8_mod.root",
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


nonMenuBrnaches = [
    "HLT_PFHT320PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v1",
    "HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p25_v1",
    "HLT_PFHT350PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v1",
    "HLT_PFHT350PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p25_v1",
    "HLT_PFHT320PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_3p0_v1",
    "HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_3p25_v1",
    "HLT_PFHT350PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_3p0_v1",
    "HLT_PFHT350PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_3p25_v1",
]

pathsForMeasurement = [
    ("QuadJetHT330CSV3p25","HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p25_v1"),
    ("QuadJetHT350CSV3p00","HLT_PFHT350PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v1"),
    ("QuadJetHT350DeepCSV3p00","HLT_PFHT350PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_3p0_v1"),
    ("QuadJetHT350CSVorDeepCSV3p00",["HLT_PFHT350PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_3p0_v1","HLT_PFHT350PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v1"]),
#    ("",""),
#    ("",""),
#    ("",""),
#    ("",""),
#    ("",""),
]

TLS = 23.31 #seconds

results = {}

menuRateAll = []
menuRateErrAll = []
nMenuPassAll = []
nMenuPassErrAll = []

addnMenuPassAll = {}
addnMenuPassAllErr = {}
addMenuRateAll = {}
addMenuRateAllErr = {}

for name, path in pathsForMeasurement:
    addnMenuPassAll[name] = []
    addnMenuPassAllErr[name] = []
    addMenuRateAll[name] = []
    addMenuRateAllErr[name] = []
    
nTot = 0
for ifile, _file in enumerate(inputfiles):
    print "---------------------------------------------"
    Rinput = ROOT.TFile.Open(basepath+_file)
    tree = Rinput.Get("tree")

    nTot += tree.Draw("","")
    print "Events in file {0}: {1}".format(_file, tree.Draw("",""))

    
    BranchesinFile = tree.GetListOfBranches()

    PathsinFile = []
    MenuPaths = []
    for b in BranchesinFile:
        if b.GetName().startswith("HLT_"):
            PathsinFile.append(b.GetName())
            if  b.GetName() not in nonMenuBrnaches:
                MenuPaths.append(b.GetName())
                #print b.GetName()

    menuSel = "HLT_FullMenu > 0"
    
    nMenuPass = tree.Draw("",menuSel)
    print nMenuPass
    print tree.Draw("","HLT_FullMenu == 0")
    nMenuPassErr = sqrt(nMenuPass)
    menuRate =  lumiSF * PS * (float(nMenuPass) / (nLS *TLS) )
    menuRateErr = lumiSF * PS * (float(nMenuPassErr) / (nLS *TLS) )

    menuRateAll.append(menuRate)
    menuRateErrAll.append(menuRateErr)
    nMenuPassAll.append(nMenuPass)
    nMenuPassErrAll.append(nMenuPassErr)
    
    for name, path in pathsForMeasurement:
        if isinstance(path, list):
            pathsel = "("
            for p in path:
                pathsel += "{0} > 0 || ".format(p)
            pathsel = pathsel[:-3]+")"
        else:
            pathsel = "( {0} > 0 )".format(path)
        
        nAddMenuPass = tree.Draw("","{0} || {1}".format(menuSel, pathsel))
        print name, nAddMenuPass, pathsel
        nAddMenuPassErr = sqrt(nAddMenuPass)
        addMenuRate =  lumiSF * PS * (float(nAddMenuPass) / (nLS *TLS) )
        addMenuRateErr = lumiSF * PS * (float(nAddMenuPassErr) / (nLS *TLS) )

        addnMenuPassAll[name].append(nAddMenuPass)
        addnMenuPassAllErr[name].append(nAddMenuPassErr)
        addMenuRateAll[name].append(addMenuRate)
        addMenuRateAllErr[name].append(addMenuRateErr)

                                


print "---------------------------------------------"
print "---------------------------------------------"
print "---------------------------------------------"
print "Events over all Dataset: {0}".format(nTot)
#Mean Rate of the full menu

meanMenu = 0
errorMenu = 0
for ival, val in enumerate(menuRateAll):
    meanMenu += val
    errorMenu += menuRateErrAll[ival]*menuRateErrAll[ival]
meanMenu = meanMenu/len(menuRateAll)
errorMenu = (1.0/len(menuRateAll)) * sqrt(errorMenu)
print "{0:>40} -> Mean rate {1:05.2f} +- {2:04.2f}".format("Menu", meanMenu, errorMenu)
print "---------------------------------------------"
print "----------------- Pure Rates ----------------"
for name, path in pathsForMeasurement:
    mean = 0
    error = 0
    for ival, val in enumerate(addMenuRateAll[name]):
        mean += val
        error += addMenuRateAllErr[name][ival]*addMenuRateAllErr[name][ival]
    mean = mean/len(addMenuRateAll[name])
    error = (1.0/len(addMenuRateAll[name])) * sqrt(error)
    pureRate = mean - meanMenu
    pureRateErr = sqrt(errorMenu*errorMenu + error*error)
    
    print "{0:>40} -> Pure Rate: {1:05.2f} +- {2:04.2f}".format(name, pureRate, pureRateErr)
    
