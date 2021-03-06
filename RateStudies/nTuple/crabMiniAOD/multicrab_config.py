#Define the datasets the following:
#list with
#     0th element: name
#     1st element: tuple containing primary and secondary DAS dataset name
#     2nd element: 0 if Data, 1 if MC
Data_RunF = [
    ["HLT_RateEst2018_v5",
     #("/EphemeralHLTPhysics1/Run2017F-PromptReco-v1/MINIAOD", "/EphemeralHLTPhysics1/Run2017F-v1/RAW"),
     ("/EphemeralHLTPhysics1/Run2017F-PromptReco-v1/AOD", "/EphemeralHLTPhysics1/Run2017F-v1/RAW"),
     "_EphemeralHLTPhysics1_RunF",
     True],
#    ["HLT_RateEst2018_v4",
#     #("/EphemeralHLTPhysics2/Run2017F-PromptReco-v1/MINIAOD", "/EphemeralHLTPhysics2/Run2017F-v1/RAW"),
#     ("/EphemeralHLTPhysics2/Run2017F-PromptReco-v1/AOD", "/EphemeralHLTPhysics2/Run2017F-v1/RAW"),
#     "_EphemeralHLTPhysics2_RunF",
#     True],
#    ["HLT_RateEst2018_v4",
#     #("/EphemeralHLTPhysics3/Run2017F-PromptReco-v1/MINIAOD", "/EphemeralHLTPhysics3/Run2017F-v1/RAW"),
#     ("/EphemeralHLTPhysics3/Run2017F-PromptReco-v1/AOD", "/EphemeralHLTPhysics3/Run2017F-v1/RAW"),
#     "_EphemeralHLTPhysics3_RunF",
#     True],
#    ["HLT_RateEst2018_v4",
#     #("/EphemeralHLTPhysics4/Run2017F-PromptReco-v1/MINIAOD", "/EphemeralHLTPhysics4/Run2017F-v1/RAW"),
#     ("/EphemeralHLTPhysics4/Run2017F-PromptReco-v1/AOD", "/EphemeralHLTPhysics4/Run2017F-v1/RAW"),
#     "_EphemeralHLTPhysics4_RunF",
#     True],
#    ["HLT_RateEst2018_v4",
#     #("/EphemeralHLTPhysics5/Run2017F-PromptReco-v1/MINIAOD", "/EphemeralHLTPhysics5/Run2017F-v1/RAW"),
#     ("/EphemeralHLTPhysics5/Run2017F-PromptReco-v1/AOD", "/EphemeralHLTPhysics5/Run2017F-v1/RAW"),
#     "_EphemeralHLTPhysics5_RunF",
#     True],
#    ["HLT_RateEst2018_v4",
#     #("/EphemeralHLTPhysics6/Run2017F-PromptReco-v1/MINIAOD", "/EphemeralHLTPhysics6/Run2017F-v1/RAW"),
#     ("/EphemeralHLTPhysics6/Run2017F-PromptReco-v1/AOD", "/EphemeralHLTPhysics6/Run2017F-v1/RAW"),
#     "_EphemeralHLTPhysics6_RunF",
#     True],
#    ["HLT_RateEst2018_v4",
#     #("/EphemeralHLTPhysics7/Run2017F-PromptReco-v1/MINIAOD", "/EphemeralHLTPhysics7/Run2017F-v1/RAW"),
#     ("/EphemeralHLTPhysics7/Run2017F-PromptReco-v1/AOD", "/EphemeralHLTPhysics7/Run2017F-v1/RAW"),
#     "_EphemeralHLTPhysics7_RunF",
#     True],
#    ["HLT_RateEst2018_v4",
#     #("/EphemeralHLTPhysics8/Run12017F-PromptReco-v1/MINIAOD", "/EphemeralHLTPhysics8/Run2017F-v1/RAW"),
#     ("/EphemeralHLTPhysics8/Run2017F-PromptReco-v1/AOD", "/EphemeralHLTPhysics8/Run2017F-v1/RAW"),
#     "_EphemeralHLTPhysics8_RunF",
#     True],
]

MC_ttH = [
    ["HLT_RateEst2018_v5",
     ("/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/RunIISummer17DRStdmix-NZSFlatPU28to62_92X_upgrade2017_realistic_v10-v1/AODSIM","/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/RunIISummer17DRStdmix-NZSFlatPU28to62_92X_upgrade2017_realistic_v10-v1/GEN-SIM-RAW"),
     "_ttHSignal",
     False]
]

MC_HH = [
    ["HLT_RateEst2018_v5",
     ("/GluGluToRSGravitonToHHTo4B_M-300_narrow_13TeV-madgraph/RunIISummer17DRStdmix-NZSFlatPU28to62_92X_upgrade2017_realistic_v10-v1/AODSIM","/GluGluToRSGravitonToHHTo4B_M-300_narrow_13TeV-madgraph/RunIISummer17DRStdmix-NZSFlatPU28to62_92X_upgrade2017_realistic_v10-v1/GEN-SIM-RAW"),
     "_HH300-Signal",
     False],
    ["HLT_RateEst2018_v5",
     ("/GluGluToHHTo4B_node_SM_13TeV-madgraph/RunIISummer17DRStdmix-NZSFlatPU28to62_92X_upgrade2017_realistic_v10-v1/AODSIM","/GluGluToHHTo4B_node_SM_13TeV-madgraph/RunIISummer17DRStdmix-NZSFlatPU28to62_92X_upgrade2017_realistic_v10-v1/GEN-SIM-RAW"),
     "_HHSM-Signal",
     False],
    ["HLT_RateEst2018_v5",
     ("/GluGluToRSGravitonToHHTo4B_M-450_narrow_13TeV-madgraph/RunIISummer17DRStdmix-NZSFlatPU28to62_92X_upgrade2017_realistic_v10-v1/AODSIM","/GluGluToRSGravitonToHHTo4B_M-450_narrow_13TeV-madgraph/RunIISummer17DRStdmix-NZSFlatPU28to62_92X_upgrade2017_realistic_v10-v1/GEN-SIM-RAW"),
     "_HH450-Signal",
     False],
]


datasets = MC_ttH+MC_HH
print datasets
prefix = "_AOD_ALL_resub"

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    from CRABClient.UserUtilities import config
    config = config()
    
    for dataset in datasets:
        name = dataset[0]
        config.section_("General")
        config.General.workArea = 'crab_' + name + prefix 
        config.General.transferLogs=True
#       config.General.requestName = name+"_"+dataset.replace('/',"_")
        config.General.requestName = name + prefix + "_" + dataset[1][0].split('/')[1].split("-")[0] + dataset[2]

        config.section_("JobType")
#        config.JobType.numCores = 4
        config.JobType.numCores = 4
        config.JobType.maxMemoryMB = 10000
        config.JobType.maxJobRuntimeMin = 720
        config.JobType.pluginName = 'Analysis'
        config.JobType.psetName = 'crab_fake_pset.py'
        config.JobType.scriptExe = 'crab_script.sh'
        import os
        os.system("tar czf python.tar.gz --dereference --directory $CMSSW_BASE python")
        os.system("voms-proxy-info -path | xargs -i  cp {}  .")
        config.JobType.inputFiles = [
            'hlt_dump_miniAOD.py',
            'hltMC_dump_miniAOD.py',
            'fwlite_config.py',
            'script.py',
            'utils.py',
            'python.tar.gz',
        ]
        
        config.section_("Data")
        config.Data.inputDBS = 'global'

        if dataset[3] is False:
            config.Data.splitting = 'LumiBased'
            config.Data.unitsPerJob = 20 ##FIXME: use 20
            config.Data.totalUnits = -1 #10*config.Data.unitsPerJob #FIXME: use -1
        else:
            config.Data.splitting = 'LumiBased'
            config.Data.unitsPerJob = 20 ##FIXME: use 20
            config.Data.totalUnits = -1 #10*config.Data.unitsPerJob #FIXME: use -1
        config.Data.outLFNDirBase = '/store/user/koschwei/' + name
        config.Data.publication = False
        #if dataset[3]:
            #config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PromptReco/Cert_294927-304120_13TeV_PromptReco_Collisions17_JSON.txt'
            #    config.Data.lumiMask = '/afs/cern.ch/work/k/koschwei/public/test/CMSSW_9_2_12_patch1/src/HLTBTagging/nTuples/PU28to63_Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'
        if dataset[3] is True:
            config.Data.lumiMask = 'json_DCS_305636_Reduced.txt'
            print "Using lumi mask "+ config.Data.lumiMask 
        config.Data.inputDataset = dataset[1][0]
        config.Data.secondaryInputDataset = dataset[1][1]
#       config.Data.publishDataName = config.General.requestName
        config.Data.outputDatasetTag = name
        config.Data.allowNonValidInputDataset = True
        config.Site.blacklist = ['T0_*']
        if True:
            config.Data.ignoreLocality = True
            config.Site.whitelist = ["T2_CH_*","T1_DE_*","T2_DE_*","T1_FR_*","T2_FR_*","T2_RU_*"]
        #config.Site.blacklist = ['T2_BR_UERJ', 'T2_TR_MET', 'T2_RU_SINP', 'T2_RU_PNPI', 'T3_RU_FIAN', 'T3_US_MIT', 'T3_UK_London_UCL', 'T3_US_UCD', 'T3_CO_Uniandes', 'T3_US_Princeton_ARM', 'T3_ES_Oviedo', 'T3_US_N', 'T3_US_NotreDame', 'T3_KR_KISTI', 'T3_IN_PUHEP', 'T3_UK_ScotGrid_ECDF', 'T2_IT_Rome', 'T2_MY_UPM_BIRUNI', 'T2_TH_CUNSTDA', 'T3_CH_CERN_HelixNebula', 'T3_US_Princeton_ICSE', 'T3_IN_TIFRCloud', 'T0_CH_CERN', 'T3_GR_IASA', 'T3_CN_PK', 'T3_US_Kansas', 'T3_IR_IPM', 'T3_US_JH', 'T3_BY_NCPHEP', 'T3_US_FS', 'T3_KR_UOS', 'T3_CH_PSI']
        #For Run C
        #config.Site.blacklist = ['T1_IT_CNAF', 'T2_BR_UERJ', 'T2_RU_SINP', 'T2_PK_NCP', 'T2_RU_PNPI', 'T3_RU_FIAN', 'T3_US_MIT', 'T3_UK_London_UCL', 'T3_US_UCD', 'T3_CO_Uniandes', 'T2_PT_NCG_Lisbon', 'T3_ES_Oviedo', 'T3_US_N', 'T3_US_NotreDame', 'T3_KR_KISTI', 'T3_IN_PUHEP', 'T2_IT_Rome',  'T2_TH_CUNSTDA',  'T3_GR_IASA', 'T3_CN_PK', 'T3_US_Kansas', 'T3_IR_IPM', 'T2_RU_ITEP', 'T3_US_JH', 'T3_BY_NCPHEP', 'T3_US_FS', 'T3_KR_UOS', 'T3_CH_PSI']
        #config.Site.ignoreGlobalBlacklist = True
        #config.Site.whitelist = ["T1_*","T2_RU_ITEP"]
        
        config.section_("Site")
        config.Site.storageSite = "T2_CH_CSCS"
        #config.Site.storageSite = "T3_CH_PSI"
        print "submitting ",dataset
        crabCommand('submit', config = config,)
        print "DONE ",dataset
    
