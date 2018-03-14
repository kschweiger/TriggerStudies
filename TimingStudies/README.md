# Timing studies

## TestHLT Configuration


GRun Reference Menu
```bash
hltGetConfiguration /users/koschwei/CMSSW_10_0_3/GRun_Copy_V14 \
--globaltag 100X_dataRun2_relval_ForTSG_v1 \
--input file:/data/user/ecarrera/timing_data/skim_Ephemeral_305636/Ephemeral_PU56-58_305636000.root \
--process TIMING --full --offline --customise HLTrigger/Configuration/customizeHLTforCMSSW.customiseFor2017DtUnpacking \
--max-events 30000 --output none --data --timing > hltGRun.py
```


Menu for proposal Option A
```bash
hltGetConfiguration /users/koschwei/CMSSW_10_0_3/GRunV14_OptA \
--globaltag 100X_dataRun2_relval_ForTSG_v1 \
--input file:/data/user/ecarrera/timing_data/skim_Ephemeral_305636/Ephemeral_PU56-58_305636000.root \
--process TIMING --full --offline --customise HLTrigger/Configuration/customizeHLTforCMSSW.customiseFor2017DtUnpacking \
--max-events 30000 --output none --data --timing > hltOptA.py
```

Menu for proposal Option B
```bash
hltGetConfiguration /users/koschwei/CMSSW_10_0_3/GRunV14_OptB \
--globaltag 100X_dataRun2_relval_ForTSG_v1 \
--input file:/data/user/ecarrera/timing_data/skim_Ephemeral_305636/Ephemeral_PU56-58_305636000.root \
--process TIMING --full --offline --customise HLTrigger/Configuration/customizeHLTforCMSSW.customiseFor2017DtUnpacking \
--max-events 30000 --output none --data --timing > hltOptB.py
```

Add this to the config
```python
process.PrescaleService.lvl1DefaultLabel = "1.6e34"
process.PrescaleService.forceDefault = True
```

## Setup

```bash
cmsrel CMSSW_10_0_3
cd CMSSW_10_0_3/src
cmsenv
git cms-addpkg HLTrigger/Configuration

git clone git@github.com:cms-steam/TimingScripts.git

# Dependencies and Compilation
git cms-checkdeps -A -a
scram b -j 6
rehash
	
	
```
