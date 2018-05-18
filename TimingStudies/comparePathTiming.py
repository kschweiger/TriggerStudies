import ROOT
from copy import deepcopy
#################################
# User input
inputfiles = [
    "V33/Reference/DQM_V0001_R000305636__HLT__FastTimerService__All.root",
    "V33/Proposal/DQM_V0001_R000305636__HLT__FastTimerService__All.root",
#    "OptA2/DQM_V0001_R000305636__HLT__FastTimerService__All.root",
#    "OptB/DQM_V0001_R000305636__HLT__FastTimerService__All.root",
#    "OptB/DQM_V0001_R000305636__HLT__FastTimerService__All.root",
    ]

paths = [
    "HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v7",
    "HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v1",
#    "HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p25_v1",
#    "HLT_PFHT350PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v1",
#    "HLT_PFHT350PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_3p0_v1",
    ]

run = "305636"
process = "TIMING"
#################################

ROOT.TH1.SetDefaultSumw2(True)
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)


histos = []
for _ifile, _file in enumerate(inputfiles):
    rfile = ROOT.TFile.Open(_file)
    print rfile
    hName = "DQMData/Run %s/HLT/Run summary/TimerService/process %s paths/path %s/path time_real" % (run,process,paths[_ifile])
    print hName
    histos.append(deepcopy(rfile.Get(hName)))
    print histos[_ifile]
    
print histos

leg = ROOT.TLegend(0.2,0.5,0.9,0.9,"")
leg.SetBorderSize(0)
leg.SetFillStyle(0)
color=1

c = ROOT.TCanvas()
c.SetLogy()

for ih, h in enumerate(histos):
    h.SetLineColor(color)
    if color==1:
        h.Draw("histo")
        h.SetTitle("")
    else:
        h.Draw("same histo")

    leg.AddEntry(h,paths[ih],"l")
    color += 1

    
leg.Draw("same")
c.Print("PathTotal_PathComparison_2.pdf")

