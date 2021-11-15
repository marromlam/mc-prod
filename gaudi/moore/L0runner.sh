source /cvmfs/lhcb.cern.ch/lib/LbEnv
lb-set-platform x86_64-slc6-gcc49-opt

lb-run Moore/${MOORE_VERSION} gaudirun.py \
${APPCONFIGOPTS}/L0App/L0AppSimProduction.py \
${APPCONFIGOPTS}/L0App/L0AppTCK-0x160F.py \
${APPCONFIGOPTS}/L0App/ForceLUTVersionV8.py \
${APPCONFIGOPTS}/L0App/DataType-${YEAR}.py \
${APPCONFIGOPTS}/Persistency/Compression-ZLIB-1.py \
${JOB_FILE} \
gaudi/Tags.py
