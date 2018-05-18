import ROOT


ROOT.TH1.SetDefaultSumw2(True)
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)


#inputfile = "/mnt/t3nfs01/data01/shome/koschwei/scratch/HLT2018Tuning/RateEstimation/ttH/FullRun/ttH_994.root"
inputfile = "/mnt/t3nfs01/data01/shome/koschwei/scratch/RateEstttH/v5/ttHv5.root"

FHSel = "Sum$(genJets_mcFlavour == 11) == 0 && Sum$(genJets_mcFlavour == 13) == 0 && Sum$(genJets_mcFlavour == 15) == 0"

varLabels = [
    "online PF HT", "online PF nJets", "online PF nCSVM",
    "offline HT", "offline nJets", "offline nCSVM",    
]
varBinning = [
    (60,0,1200),
    (14,1.5,15.5),
    (7,-0.5,6.5),
    (60,0,1200),
    (14,1.5,15.5),
    (7,-0.5,6.5)
]
varsToPlot = [
    "Sum$(pfJets_pt * (pfJets_pt > 30 && abs(pfJets_eta) < 2.4))",
    "Sum$(pfJets_pt > 30 && abs(pfJets_eta) < 2.4)",
    "Sum$(pfJets_pt > 30 && abs(pfJets_eta) < 2.4 && pfJets_csv > 0.8484)",
    "Sum$(offCleanJets_pt * (offCleanJets_pt > 30 && abs(offCleanJets_eta) < 2.4))",
    "Sum$(offCleanJets_pt > 30 && abs(offCleanJets_eta) < 2.4)",
    "Sum$(offCleanJets_pt > 30 && abs(offCleanJets_eta) < 2.4 && offCleanJets_csv > 0.8484)"
]

rFile = ROOT.TFile.Open(inputfile) 
tree = rFile.Get("tree")

c = ROOT.TCanvas("c1","c1", 800, 600)

for ivar, var in enumerate(varsToPlot):
    label = varLabels[ivar]
    nbins = varBinning[ivar][0]
    binstart = varBinning[ivar][1]
    binend = varBinning[ivar][2]

    h1 = ROOT.TH1F(label, label, nbins, binstart, binend)

    tree.Project(label,var,FHSel)


    h1.SetLineWidth(3)
    h1.SetTitle("")
    h1.GetYaxis().SetTitle("Normalized units")
    h1.GetYaxis().SetTitleOffset(1.4)
    print h1.GetYaxis().GetTitleOffset()
    h1.GetXaxis().SetTitle(label)
    h1.DrawNormalized("histo")
    

    c.Update()
    c.Print("FHRegion_"+label+".pdf")
    #raw_input()
    
    
