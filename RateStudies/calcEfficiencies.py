from __future__ import division

import ROOT
from math import sqrt


ROOT.TH1.SetDefaultSumw2(True)
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

#################################
# User input

inputfile = "/mnt/t3nfs01/data01/shome/koschwei/scratch/HLT2018Tuning/RateEstimation/offline150318/ttH/sumTree.root"
#inputfile = "/mnt/t3nfs01/data01/shome/koschwei/scratch/HLT2018Tuning/RateEstimation/offline150318/HH/SM/sumTree.root"
#inputfile = "/mnt/t3nfs01/data01/shome/koschwei/scratch/HLT2018Tuning/RateEstimation/offline150318/HH/300/sumTree.root"
#inputfile = "/mnt/t3nfs01/data01/shome/koschwei/scratch/HLT2018Tuning/RateEstimation/offline150318/HH/450/sumTree.root"

FHSel = "Sum$(genJets_mcFlavour == 11) == 0 && Sum$(genJets_mcFlavour == 13) == 0 && Sum$(genJets_mcFlavour == 15) == 0 "
#FHSel = "1"
OffSel = [
    "1",
#    "Sum$(offJets_pt > 30 && abs(offJets_eta) < 2.4) >= 4 && Sum$(offJets_pt > 30 && abs(offJets_eta) < 2.4 && offJets_deepcsv > 0.4941) >=4  && (Alt$(offJets_pt[5],0) > 30)",
#    "Sum$(offJets_pt > 30 && abs(offJets_eta) < 2.4) >= 4 && Sum$(offJets_pt * (offJets_pt > 30 && abs(offJets_eta) < 2.4)) > 400 && Sum$(offJets_pt > 30 && abs(offJets_eta) < 2.4 && offJets_deepcsv > 0.4941) > 3",
#   "Sum$(offJets_pt > 30 && abs(offJets_eta) < 2.4) >= 6 && Sum$(offJets_pt * (offJets_pt > 30 && abs(offJets_eta) < 2.4)) > 450 && Sum$(offJets_pt > 30 && abs(offJets_eta) < 2.4 && offJets_deepcsv > 0.4941) >= 2",
#    "Sum$(offJets_pt > 30 && abs(offJets_eta) < 2.4) > 7 && Sum$(offJets_pt * (offJets_pt > 30 && abs(offJets_eta) < 2.4)) > 500 && Sum$(offJets_pt > 30 && abs(offJets_eta) < 2.4 && offJets_deepcsv > 0.4941) > 3 && (Alt$(offJets_pt[5],0) > 40)"
]


paths = [
    ("SixJetsSingleB","HLT_PFHT430_SixPFJet40_PFBTagCSV_1p5_v7"),
    ("SixJetsDoubleB","HLT_PFHT380_SixPFJet32_DoublePFBTagCSV_2p2_v7"),
#    ("SixJetsSingleBDeepCSV","HLT_PFHT380_SixPFJet32_DoublePFBTagDeepCSV_2p2_v6"),
    ("QuadJet300CSV3p00","HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v7"),
    ("2017Config", ["HLT_PFHT430_SixPFJet40_PFBTagCSV_1p5_v7","HLT_PFHT380_SixPFJet32_DoublePFBTagCSV_2p2_v7", "HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v7" ]),
    ("SixJet", ["HLT_PFHT430_SixPFJet40_PFBTagCSV_1p5_v7","HLT_PFHT380_SixPFJet32_DoublePFBTagCSV_2p2_v7" ]),
    ("SixJetOrQuadJet300CSV3p00", ["HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v7", "HLT_PFHT380_SixPFJet32_DoublePFBTagCSV_2p2_v7"]),
    ("QuadJet3503p00CSVORDeepCSV", ["HLT_PFHT350PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v1","HLT_PFHT350PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_3p0_v1"]),
#    ("QuadJet3503p00CSVORDeepCSVSixJet", ["HLT_PFHT350PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v1","HLT_PFHT350PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_3p0_v1","HLT_PFHT380_SixPFJet32_DoublePFBTagCSV_2p2_v7"]),
#    ("QuadJet330csv3p25OrSixJetsDoubleB",["HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p25_v1","HLT_PFHT380_SixPFJet32_DoublePFBTagCSV_2p2_v7"]),
#    ("QuadJet350ORSixJetDoubleBorSixJetSingleB", ["HLT_PFHT380_SixPFJet32_DoublePFBTagCSV_2p2_v7", "HLT_PFHT430_SixPFJet40_PFBTagCSV_1p5_v7","HLT_PFHT350PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v1"]),
##    ("QuadJet320CSV3p00","HLT_PFHT320PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v1"),
#    ("QuadJet320CSV3p25","HLT_PFHT320PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p25_v1"),
 #   ("QuadJet320CSV3p75","HLT_PFHT320PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p75_v1"),
  #  ("QuadJet320CSV4p50","HLT_PFHT320PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_4p5_v1"),
#    ("QuadJet330CSV3p00","HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v1"),
#    ("QuadJet330CSV3p25","HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p25_v1"),
#    ("QuadJet330CSV3p75","HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p75_v1"),
#    ("QuadJet330CSV4p50","HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_4p5_v1"),
#    ("QuadJet340CSV3p00","HLT_PFHT340PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v1"),
#    ("QuadJet340CSV3p25","HLT_PFHT340PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p25_v1"),
#    ("QuadJet340CSV3p75","HLT_PFHT340PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p75_v1"),
#    ("QuadJet340CSV4p50","HLT_PFHT340PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_4p5_v1"),
##    ("QuadJet350CSV3p00","HLT_PFHT350PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v1"),
#    ("QuadJet350CSV3p25","HLT_PFHT350PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p25_v1"),
#    ("QuadJet350CSV3p75","HLT_PFHT350PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p75_v1"),
#    ("QuadJet350CSV4p50","HLT_PFHT350PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_4p5_v1"),
#    ("QuadJet320DeepCSV3p00","HLT_PFHT320PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_3p0_v1"),
#    ("QuadJet320DeepCSV3p25","HLT_PFHT320PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_3p25_v1"),
#    ("QuadJet320DeepCSV3p75","HLT_PFHT320PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_3p75_v1"),
 #   ("QuadJet320DeepCSV4p50","HLT_PFHT320PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v1"),#
 #   ("QuadJet330DeepCSV3p00","HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_3p0_v1"),
#   ("QuadJet330DeepCSV3p25","HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_3p25_v1"),
#   ("QuadJet330DeepCSV3p75","HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_3p75_v1"),
#    ("QuadJet330DeepCSV4p5","HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v1"),
#    ("QuadJet335DeepCSV4p5","HLT_PFHT335PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v1"),
#  ("QuadJet330DeepCSV4p50","HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v1"),
   # ("QuadJet340DeepCSV3p00","HLT_PFHT340PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_3p0_v1"),
 #   ("QuadJet340DeepCSV3p25","HLT_PFHT340PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_3p25_v1"),
 #   ("QuadJet340DeepCSV3p75","HLT_PFHT340PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_3p75_v1"),
 #   ("QuadJet340DeepCSV4p50","HLT_PFHT340PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v1"),
##    ("QuadJet350DeepCSV3p00","HLT_PFHT350PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_3p0_v1"),
 #   ("QuadJet350DeepCSV3p25","HLT_PFHT350PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_3p25_v1"),
  #  ("QuadJet350DeepCSV3p75","HLT_PFHT350PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_3p75_v1"),
   # ("QuadJet350DeepCSV4p50","HLT_PFHT350PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v1"),

]



#
#################################
rFile = ROOT.TFile.Open(inputfile) 
tree = rFile.Get("tree")
print "-------------------------------------------------------------------------------"
print inputfile

BranchesinFile = tree.GetListOfBranches()

for selection in OffSel:
    print "---------------------------------------------------"
    print "Using offline selection:"
    print selection
    print "---------------------------------------------------"
    for name, path in paths:
        #print "Denominator: {0} && {1}".format(FHSel, selection)
        denom = tree.Draw("","{0} && {1}".format(FHSel, selection))
        errdenom = sqrt(denom)
        if isinstance(path, list):
            pathsel = "("
            for p in path:
                pathsel += "{0} > 0 || ".format(p)
            pathsel = pathsel[:-3]+")"
            num = tree.Draw("","{0} && {1} && {2}".format(FHSel, selection, pathsel))
            #print "Numerator: {0} && {1} && {2}".format(FHSel, selection, pathsel)
        else:
            num = tree.Draw("","{0} && {1} && ({2} > 0)".format(FHSel, selection, path))
            #print "Numerator: {0} && {1} && ({2} > 0)".format(FHSel, selection, path)
        errnum = sqrt(num)
        eff = num/denom
        erreff = sqrt( eff*eff * ( (errnum/num)*(errnum/num) + (errdenom/denom)*(errdenom/denom) ) )
        #print "{0}: pass Sel: {1} Pass Trig: {2}".format(name, denom, num)
        print "{0:>50}: {1:1.4f} +- {2:1.4f}".format(name, eff*100, erreff*100)
