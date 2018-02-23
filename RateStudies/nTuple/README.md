# nTuples for HLT rate studies

First run the hltGetConfiguration script
```bash
hltGetConfiguration /users/koschwei/CMSSW_10_0_2/HLT_2018Tuning \
--setup /dev/CMSSW_10_0_0/GRun --globaltag 100X_dataRun2_relval_ForTSG_v1 \
--input file:/mnt/t3nfs01/data01/shome/koschwei/scratch/EphemeralHLTPhysics1_Run2017E-v1/3A521513-B9AD-E711-9D2D-02163E019E38.root \
--process MYHLT --full --offline --customise HLTrigger/Configuration/customizeHLTforCMSSW.customiseFor2017DtUnpacking \
--prescale none --max-events 10 --output none --data > hlt.py
```

## Running only on RAW w/ ntupler.py

Run
```bash
edmConfigDump hlt.py > hlt_dump.py
```

Remove
```python
process.DQMOutput = cms.EndPath(process.dqmOutput)
```

Add
```python
process.hltOutputFULL = cms.OutputModule("PoolOutputModule",
									 dataset = cms.untracked.PSet(),
									 fileName = cms.untracked.string('./hltOut.root'),
									 outputCommands = cms.untracked.vstring('drop *',
																			"keep edmTriggerResults*_*_*_*")

)
process.FULLOutput = cms.EndPath(process.hltOutputFULL)
```

## Running on RAW+miniAOD/AOD w/ nTuplerMiniAOD.py

```bash
edmConfigDump hlt.py > hlt_dump_miniAOD.py
```

Remove
```python
process.DQMOutput = cms.EndPath(process.dqmOutput)
```

Add
Check dataformt for VID producer!
```python 
from PhysicsTools.SelectorUtils.tools.vid_id_tools import *
# turn on VID producer, indicate data format  to be
# DataFormat.AOD or DataFormat.MiniAOD, as appropriate 
dataFormat = DataFormat.miniAOD

switchOnVIDElectronIdProducer(process, dataFormat)

# define which IDs we want to produce
my_id_modules = ['RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Summer16_80X_V1_cff']

#add them to the VID producer
for idmod in my_id_modules:
	setupAllVIDIdsInModule(process,idmod,setupVIDElectronSelection)
process.p = cms.Path(process.egmGsfElectronIDSequence)


process.hltOutputFULL = cms.OutputModule("PoolOutputModule",
					dataset = cms.untracked.PSet(),
					fileName = cms.untracked.string('./cmsswPreProcessing.root'),
					outputCommands = cms.untracked.vstring('drop *',
					'keep *Egamma*_*_*_*',
					'keep bool*ValueMap*_*Electron*_*_*',
					'keep l1t*_*_*_*',
					'keep *_*Ht*_*_*',
					'keep *Jet*_*_*_*',
					'keep *Electron*_*_*_*',
					'keep *Muon*_*_*_*',
					'keep *Track*_*_*_*',
					'drop *Track*_hlt*_*_*',
					'drop SimTracks_*_*_*',
					'keep *SuperCluster*_*_*_*',
					'keep *MET*_*_*_*',
					'keep *Vertex*_*_*_*',
					#######
					'keep *_genParticles_*_*',#AOD
					'keep *_prunedGenParticles_*_*',#MINIAOD
					#######
					'keep *genParticles_*_*_*',
					'keep *Trigger*_*_*_*',
					'keep recoJetedmRefToBaseProdTofloatsAssociationVector_*_*_*',
					#######
					'keep *_addPileupInfo_*_*', #AOD
					'keep *_slimmedAddPileupInfo_*_*',#MINIAOD
					#######
					'drop *_*Digis*_*_*',
					'drop triggerTriggerEvent_*_*_*',
					'keep edmTriggerResults*_*_*_*',
					'keep *_hltGtStage2Digis_*_*',
					'keep *_generator_*_*')
)
process.FULLOutput = cms.EndPath(process.hltOutputFULL)

```
