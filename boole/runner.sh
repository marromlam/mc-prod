source /cvmfs/lhcb.cern.ch/lib/LbEnv
lb-set-platform x86_64-slc6-gcc49-opt

lb-run Boole/${BOOLE_VERSION} gaudirun.py \
${APPCONFIGOPTS}/Boole/Default.py \
${APPCONFIGOPTS}/Boole/EnableSpillover.py \
${APPCONFIGOPTS}/Boole/DataType-${YEAR}.py \
${APPCONFIGOPTS}/Boole/Boole-SetOdinRndTrigger.py \
${APPCONFIGOPTS}/Persistency/Compression-ZLIB-1.py \
${JOB_FILE} \
Tags.py

