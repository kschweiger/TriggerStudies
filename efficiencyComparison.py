import ROOT
ROOT.TH1.SetDefaultSumw2(True)
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

rfile = ROOT.TFile.Open("/mnt/t3nfs01/data01/shome/koschwei/scratch/DONOTREMOVE/HLTDev/2018/RateEstimation/ttH/ttH_994.root")
tree = rfile.Get("tree")

#2017 configuration
numeratorSel2017 = "HLT_PFHT300PT30_QuadPFJet_75_60_45_40_v7 && HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v7"
denominatorSel2017 = "HLT_PFHT300PT30_QuadPFJet_75_60_45_40_v7"

#2018 configuration
numeratorSel2018 = "HLT_PFHT330PT30_QuadPFJet_75_60_45_40_v7 && HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_4p5_v1"
denominatorSel2018 = "HLT_PFHT330PT30_QuadPFJet_75_60_45_40_v7"

FHSel = "Sum$(genJets_mcFlavour == 11) == 0 && Sum$(genJets_mcFlavour == 13) == 0 && Sum$(genJets_mcFlavour == 15) == 0"

binning = {
    "csv":(20,0,1),
    "deepcsv":(20,0,1),
    "pt":(80,0,400), 
    }

c1 = ROOT.TCanvas("c1","c1",1600,1280)

c1.SetTopMargin(0.06)
c1.SetRightMargin(0.04)
c1.SetLeftMargin(0.1)
c1.SetBottomMargin(0.1)

c1.cd()
vars2plot = ["deepcsv"]#, "csv"]#,"pt"]

collections = [ ("deepcsvOrdered","offCleanDeepCSVJets", "jet with third highest DeepCSV"),
                #("csvOrdered","offCleanCSVJets", "jet with third highest CSV")
]

for identifier ,collection, title in collections:
    print "Processing collection",collection
    for var in vars2plot:#
        print "Processing var",var
        hdenom2017 = ROOT.TH1F("hdenom2017"+identifier+var, "hdenom2017"+identifier+var, binning[var][0], binning[var][1], binning[var][2])
        hdenom2018 = ROOT.TH1F("hdenom2018"+identifier+var, "hdenom2018"+identifier+var, binning[var][0], binning[var][1], binning[var][2])
        hnum2017 = ROOT.TH1F("hnum2017"+identifier+var, "hnum2017"+identifier+var, binning[var][0], binning[var][1], binning[var][2])
        hnum2018 = ROOT.TH1F("hnum2018"+identifier+var, "hnum2018"+identifier+var, binning[var][0], binning[var][1], binning[var][2])

        hdenom2017.SetLineColor(ROOT.kBlue)
        hnum2017.SetLineColor(ROOT.kBlue)
        hdenom2018.SetLineColor(ROOT.kRed)
        hnum2018.SetLineColor(ROOT.kRed)

        hdenom2017.SetLineWidth(2)
        hnum2017.SetLineWidth(2)
        hdenom2018.SetLineWidth(2)
        hnum2018.SetLineWidth(2)

        hdenom2017.SetTitle("")
        hnum2017.SetTitle("")
        hdenom2018.SetTitle("")
        hnum2018.SetTitle("")

        if var == "deepcsv":
            name = "DeepCSV"
        elif var == "csv":
            name = "CSV"
        elif var == "pt":
            name = "#p_{T}"
        else:
            name = var

        tree.Project("hdenom2017"+identifier+var, collection+"_"+var+"[3]", denominatorSel2017 + "&&" + FHSel + "&&" + collection+"_"+var+"[3] > 0")
        tree.Project("hnum2017"+identifier+var, collection+"_"+var+"[3]", numeratorSel2017 + "&&" + FHSel + "&&" + collection+"_"+var+"[3] > 0")
        tree.Project("hdenom2018"+identifier+var, collection+"_"+var+"[3]", denominatorSel2018 + "&&" + FHSel + "&&" + collection+"_"+var+"[3] > 0")
        tree.Project("hnum2018"+identifier+var, collection+"_"+var+"[3]", numeratorSel2018 + "&&" + FHSel + "&&" + collection+"_"+var+"[3] > 0")

        gr2017 = ROOT.TGraphAsymmErrors(hnum2017, hdenom2017)
        gr2018 = ROOT.TGraphAsymmErrors(hnum2018, hdenom2018)

        gr2017.GetXaxis().SetTitle(name+" of "+title+" value")
        gr2017.GetYaxis().SetTitle("b-tagging efficiency")

        gr2017.SetMarkerColor(ROOT.kBlue)
        gr2018.SetMarkerColor(ROOT.kRed)

        for histo in [gr2017, gr2018]:
            #histo.SetLineColor(ROOT.kBlack)
            histo.SetMarkerStyle(20)
            histo.SetMarkerSize(2)  




        gr2017.Draw("AP")

        gr2017.GetHistogram().SetMaximum(1.1)
        #gr2017.GetHistogram().SetMinimum(0.0)
        gr2017.GetXaxis().SetRangeUser(binning[var][1], binning[var][2])
        gr2017.Draw("AP")

        gr2018.Draw("PSame")

        firstline = '#scale['+str(1.2)+']{#bf{CMS}} #it{Simulation}'
        cmsfistLine = ROOT.TLatex(0.15, 0.885, firstline)
        cmsfistLine.SetTextFont(42)
        cmsfistLine.SetTextSize(0.045)
        cmsfistLine.SetNDC()

        cmssecondline = ROOT.TLatex(0.15, 0.838, '#it{work in progress}')
        cmssecondline.SetTextFont(42)
        cmssecondline.SetTextSize(0.045)
        cmssecondline.SetNDC()


        sampleLabel = ROOT.TLatex(0.5, 0.955, "t#bar{t}H(b#bar{b}) all-hardonic simulation")
        sampleLabel.SetTextFont(42)
        sampleLabel.SetTextSize(0.045)
        sampleLabel.SetNDC()

        #cmsfistLine.Draw("same")
        #cmssecondline.Draw("same")
        sampleLabel.Draw("same")



        if var == "deepcsv":
            legend = ROOT.TLegend(0.25,0.2,0.97,0.35)
        else:
            legend = ROOT.TLegend(0.15,0.6,0.35,0.9)

        legend.AddEntry(gr2017, "2017 HLT path (Signal efficiency: 45.26 #pm 0.06 %)", "p")
        legend.AddEntry(gr2018, "2018 HLT path (Signal efficiency: 49.43 #pm 0.07 %)", "p")
        legend.SetBorderSize(0)
        legend.SetTextFont(42)
        legend.SetFillStyle(0)
        legend.Draw("same")
        c1.Update()


        c1.Print("bTagEfficiency_{0}_{1}.pdf".format(collection,var),"pdf")
