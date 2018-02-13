import time

import imp
from array import array

import ROOT
from DataFormats.FWLite import Handle, Events

from utils import deltaR,SetVariable,DummyClass,productWithCheck,checkTriggerIndex

def launchNtuple(fileOutput,filesInput, maxEvents, preProcess = True):
    t0 = time.time()
    
    print "Outputfile: {0}".format(fileOutput)
    print "Inputfiles: {0}".format(filesInput)
    print "MaxEvents; {0}".format(maxEvents)

    import os
    dir_ = os.getcwd()

    if preProcess:
        hltdumpFile = "hlt_dump.py"
        cmsswConfig = imp.load_source("cmsRunProcess",os.path.expandvars(hltdumpFile))
        cmsswConfig.process.maxEvents.input = maxEvents
        cmsswConfig.process.source.fileNames = filesInput

        configfile=dir_+"/mod_hlt_dump.py"
        f = open(configfile, 'w')
        f.write(cmsswConfig.process.dumpPython())
        f.close()

        runstring="{0} {1} >& {2}/cmsRun_hltDump.log".format("cmsRun",configfile, dir_)
        print "Running pre-processor: %s " %runstring
        ret=os.system(runstring)
        if ret != 0:
            print "CMSRUN failed"
            exit(ret)

    print "Time to preprocess: {0:10f} s".format(time.time()-t0)    
    print "Filesize of {0:8f} MB".format(os.path.getsize(dir_+"/hltOut.root") * 1e-6)

    f = ROOT.TFile(fileOutput,"recreate")
    tree = ROOT.TTree("tree","tree")
     
    fwLiteInputs = ["hltOut.root"]
    if len(filesInput)==0: exit
    import os.path
    if not os.path.isfile(fwLiteInputs[0]):
        raise Exception( fwLiteInputs[0] + " does not exist.")
    events = Events (fwLiteInputs)

    triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults::MYHLT")

    events.to(0)
    for event in events: break
    event.getByLabel(triggerBitLabel, triggerBits)
    names = event.object().triggerNames(triggerBits.product())
    triggerNames = names.triggerNames()
    for name in triggerNames: name = name.split("_v")[0]
    nTriggers = len(triggerNames)
    triggerVars = {}
    for trigger in triggerNames:
        triggerVars[trigger]=array( 'i', [ 0 ] )
        tree.Branch( trigger, triggerVars[trigger], trigger+'/O' )

    nEvArray = array('i', [0])
    tree.Branch( "nEvents", nEvArray, "nEvents/I")

    print "Starting event loop"
    for iev,event in enumerate(events):
        nEvArray[0] = 1
        event.getByLabel(triggerBitLabel, triggerBits)
        names = event.object().triggerNames(triggerBits.product())
        triggerspassing = []
        for i,triggerName in enumerate(triggerNames):
            index = names.triggerIndex(triggerName)
            if checkTriggerIndex(triggerName,index,names.triggerNames()):
                triggerVars[triggerName][0] = triggerBits.product().accept(index)
                if triggerName.startswith("HLT") and not ( triggerName.startswith("NoFilter") or triggerName.endswith("FirstPath") or triggerName.endswith("FinalPath")):
                    if triggerBits.product().accept(index):
                        triggerspassing.append(triggerName)
            else:
                triggerVars[triggerName][0] = 0

                
        if iev%100==1: print "Event: ",iev," done."
        tree.Fill()

    f.Write()
    f.Close()


    print "Total time: {0:10f} s".format(time.time()-t0)
    print "Filesize of {0:8f} MB".format(os.path.getsize(dir_+"/"+fileOutput) * 1e-6)

    
if __name__ == "__main__":
    inputfiles = ["file:/mnt/t3nfs01/data01/shome/koschwei/scratch/EphemeralHLTPhysics1_Run2017E-v1/E27D9132-B8AD-E711-867D-02163E013886.root"]
    outputfile = "tree.root"
    maxEvents = 100

    launchNtuple(outputfile, inputfiles, maxEvents, True)
    
