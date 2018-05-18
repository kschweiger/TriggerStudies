import ROOT


ROOT.TH1.SetDefaultSumw2(True)
#ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)


inputfile = "/mnt/t3nfs01/data01/shome/koschwei/scratch/HLT2018Tuning/RateEstimation/ttH/FullRun/ttH_994.root"
#inputfile = "/mnt/t3nfs01/data01/shome/koschwei/scratch/RateEstttH/v5/ttHv5.root"

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


triggerlist = [ "HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v7", "HLT_PFHT380_SixPFJet32_DoublePFBTagCSV_2p2_v7", "HLT_PFHT430_SixPFJet40_PFBTagCSV_1p5_v7"]

stackSel = [  "HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v7 == 1 && HLT_PFHT380_SixPFJet32_DoublePFBTagCSV_2p2_v7  == 0 && HLT_PFHT430_SixPFJet40_PFBTagCSV_1p5_v7 == 0", #only 4J3T 
              "HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v7 == 0 && HLT_PFHT380_SixPFJet32_DoublePFBTagCSV_2p2_v7  == 1 && HLT_PFHT430_SixPFJet40_PFBTagCSV_1p5_v7 == 0", #only 6J2T
              "HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v7 == 0 && HLT_PFHT380_SixPFJet32_DoublePFBTagCSV_2p2_v7  == 0 && HLT_PFHT430_SixPFJet40_PFBTagCSV_1p5_v7 == 1", #only 6J1T
              "HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v7 == 0 && HLT_PFHT380_SixPFJet32_DoublePFBTagCSV_2p2_v7  == 1 && HLT_PFHT430_SixPFJet40_PFBTagCSV_1p5_v7 == 1", #only 6J1T and 6J2T
              "HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v7 == 1 && HLT_PFHT380_SixPFJet32_DoublePFBTagCSV_2p2_v7  == 0 && HLT_PFHT430_SixPFJet40_PFBTagCSV_1p5_v7 == 1", #only 6J1T and 4J3T
              "HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v7 == 1 && HLT_PFHT380_SixPFJet32_DoublePFBTagCSV_2p2_v7  == 1 && HLT_PFHT430_SixPFJet40_PFBTagCSV_1p5_v7 == 0", #only 6J2T and 4J3T
              "HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v7 == 1 && HLT_PFHT380_SixPFJet32_DoublePFBTagCSV_2p2_v7  == 1 && HLT_PFHT430_SixPFJet40_PFBTagCSV_1p5_v7 == 1", #only 6J1T and 6J2T and 4J3T
              "HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v7 == 0 && HLT_PFHT380_SixPFJet32_DoublePFBTagCSV_2p2_v7  == 0 && HLT_PFHT430_SixPFJet40_PFBTagCSV_1p5_v7 == 0", #None
]

stackColors = [ROOT.kBlue, ROOT.kRed, ROOT.kGreen+2, ROOT.kYellow+2, ROOT.kCyan, ROOT.kMagenta, ROOT.kWhite, ROOT.kGray]

if len(stackSel) != len(stackColors):
    print "Error! Number len(stackSel) != len(stackColorse)"
    exit()

    
rFile = ROOT.TFile.Open(inputfile) 
tree = rFile.Get("tree")

c = ROOT.TCanvas("c1","c1", 800, 600)



for ivar, var in enumerate(varsToPlot):
    label = varLabels[ivar]
    nbins = varBinning[ivar][0]
    binstart = varBinning[ivar][1]
    binend = varBinning[ivar][2]
    stack = ROOT.THStack("hStack_"+label,"")
    histos = []
    for isel, sel in enumerate(stackSel):
        print "Processing stack selection {0} of {1}".format(isel, len(stackSel)-1)
        histos.append(ROOT.TH1F(label+str(isel), label+str(isel), nbins, binstart, binend))
        tree.Project(label+str(isel),var,"{0} && {1}".format(FHSel,sel))
        #histos[isel].SetLineColor(ROOT.kBlack)
        histos[isel].SetFillColor(stackColors[isel])        
        stack.Add(histos[isel])


    """    
    h1.SetLineWidth(3)
    h1.SetTitle("")
    h1.GetYaxis().SetTitle("Normalized units")
    h1.GetYaxis().SetTitleOffset(1.4)
    print h1.GetYaxis().GetTitleOffset()
    h1.GetXaxis().SetTitle(label)
    h1.DrawNormalized("histo")
    """
    stack.Draw()
    c.Update()
    #c.Print("FHRegion_"+label+".pdf")
    raw_input()

    
