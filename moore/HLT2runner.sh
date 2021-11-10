source /cvmfs/lhcb.cern.ch/lib/LbEnv
lb-set-platform x86_64-slc6-gcc49-opt

lb-run Moore/${MOORE_VERSION} gaudirun.py \
${APPCONFIGOPTS}/Moore/MooreSimProductionForSeparateL0AppStep${YEAR}.py \
${APPCONFIGOPTS}/Conditions/TCK-0x6139160F.py \
${APPCONFIGOPTS}/Moore/MooreSimProductionHlt2.py \
${APPCONFIGOPTS}/L0App/DataType-${YEAR}.py \
${APPCONFIGOPTS}/Persistency/Compression-ZLIB-1.py \
${JOB_FILE} \
Tags.py
