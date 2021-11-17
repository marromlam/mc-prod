source /cvmfs/lhcb.cern.ch/lib/LbEnv
lb-set-platform x86_64-slc6-gcc49-opt


mkdir -p ${SANDBOX}
cd ${SANDBOX}

lb-run DaVinci/${DAVINCI_VERSION} gaudirun.py \
${APPCONFIGOPTS}/DaVinci/DV-Stripping${STRIPPING_VERSION}-Stripping-MC-NoPrescaling-DST.py \
${APPCONFIGOPTS}/DaVinci/DV-RedoCaloPID-Stripping_28_24.py \
${APPCONFIGOPTS}/DaVinci/DataType-${YEAR}.py \
${APPCONFIGOPTS}/DaVinci/InputType-DST.py \
${APPCONFIGOPTS}/DaVinci/DV-RawEventJuggler-4_3-to-4_3.py \
${JOB_FILE}


cd ${MC_PROD}
