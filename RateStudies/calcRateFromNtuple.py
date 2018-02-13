import ROOT

#################################
# User input 
inputfile = "EphemeralHLTPhysics1.root"
nLS = 60236
PS = 580
#lumiSF = 405155.036 / 44863 #RunE
lumiSF = 593356.317 / 60236 #RunF
#################################

ROOT.TH1.SetDefaultSumw2(True)
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

print lumiSF

TLS = 23.31 #seconds

Rinput = ROOT.TFile.Open(inputfile)
tree = Rinput.Get("tree")

BranchesinFile = tree.GetListOfBranches()

PathsinFile = []
for b in BranchesinFile:
    if b.GetName().startswith("HLT_"):
        PathsinFile.append(b.GetName())

results = {}
for path in PathsinFile:
    nPassed = tree.Draw(path, "{0} == 1".format(path))
    nFailed = tree.Draw(path, "{0} == 0".format(path))
    rate = lumiSF * PS * (float(nPassed) / (nLS *TLS) )
    print path, rate, nPassed, nFailed
    results[path] = rate

pathpair = []
for ipath,path in enumerate(PathsinFile):
    for path2 in PathsinFile:
        if path != path2 and (path[-10:] == path2[-10:]):
            pathpair.append((path, path2))
            PathsinFile.remove(path)


for path1, path2 in pathpair:
    nPassed = tree.Draw("", "{0} == 1 || {1} == 1 ".format(path1, path2))
    rate = lumiSF * PS * (float(nPassed) / (nLS *TLS) )
    print "{0} or {1} {2}".format(path1, path2, rate)
