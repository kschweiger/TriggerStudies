# TriggerStudies

## Setup

```bash 
cmsrel CMSSW_10_0_1
cd CMSSW_10_0_1/src
cmsenv
git cms-addpkg HLTrigger/Configuration

# Dependencies and Compilation
git cms-checkdeps -A -a
scram b -j 6

git clone git@github.com:kschweiger/TriggerStudies.git
```
